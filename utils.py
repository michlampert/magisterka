import pandas as pd
from ogb.graphproppred import PygGraphPropPredDataset
import logging
import time
from models import *
from typing import Iterator, Callable, Tuple
from tqdm import tqdm
import deepchem as dc
from rdkit import Chem
from itertools import chain

logger = logging.getLogger("molecules")


def load_ogb_dataset(name: str) -> pd.DataFrame:
    dataset = PygGraphPropPredDataset(name=name)

    smiles = pd.read_csv(f"dataset/{name.replace('-', '_')}/mapping/mol.csv.gz").drop(['mol_id'], axis=1)
    return smiles, dataset.get_idx_split()


def load_tdc_dataset(module, name: str):
    data = module(name=name)
    split = data.get_split()

    train, valid, test = split["train"], split["valid"], split["test"]

    train_range = list(range(0, len(train)))
    train.index = train_range
    valid_range = list(range(len(train), len(train) + len(valid)))
    valid.index = valid_range
    test_range = list(range(len(train) + len(valid), len(train) + len(valid) + len(test)))
    test.index = test_range

    return (
        pd.concat([train, valid, test]).rename(columns={"Drug": "smiles"}),
        {"train": train_range, "valid": valid_range, "test": test_range}
    )


def featurize_with(featurizer):

    def inner(smiles):
        try:
            start = time.time()
            res = featurizer([smiles])
            if time.time() - start > 10:
                logger.warning(f"\rHeavy processing ({(time.time() - start):.1f}s) of '{smiles}'" + " " * 20)
            return res
        except RuntimeError:
            logger.warning(f"\rProblem while processing '{smiles}'" + " " * 20)
            return None

    return inner


def process(df, model, featurizer):
    with torch.no_grad():
        tqdm.pandas()
        df["features"] = df.smiles.progress_map(featurize_with(featurizer))
        df["embeddings"] = df.features.dropna().progress_map(lambda f: model(f)[0])


def get_huggingmolecules_embedders() -> Iterator[Tuple[str, Callable[[pd.DataFrame], pd.DataFrame]]]:
    for config in ["mat_masking_200k", "mat_masking_2M", "mat_masking_20M"]:
        yield (config, lambda df: process(df, StrippedMatModel.from_pretrained(config), MatFeaturizer.from_pretrained(config)))

    for config in ["grover_base", "grover_large"]:
        yield (config, lambda df: precess(df, StrippedGroverModel.from_pretrained(config), GroverFeaturizer.from_pretrained(config)))

    for config in ["rmat_4M", "rmat_4M_rdkit"]:
        yield (config, lambda df: process(df, StrippedRMatModel.from_pretrained(config), RMatFeaturizer.from_pretrained(config)))


def get_deepchem_embedders() -> Iterator[Tuple[str, Callable[[pd.DataFrame], pd.DataFrame]]]:
    model = dc.feat.Mol2VecFingerprint()

    def process(smiles):
        with torch.no_grad():
            tqdm.pandas()
            smiles["embeddings"] = smiles.smiles.progress_map(lambda f: model(f)[0])
            
    yield ("mol2vec", process)


def get_embedders() -> Iterator[Tuple[str, Callable[[pd.DataFrame], pd.DataFrame]]]:
    return chain(
        get_deepchem_embedders(),
        get_huggingmolecules_embedders(),
    )


if __name__ == "__main__":
    pass
