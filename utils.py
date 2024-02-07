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
from functools import partial

logger = logging.getLogger("molecules")


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


def process_huggingmolecules(df, model, featurizer):
    with torch.no_grad():
        tqdm.pandas()
        df["features"] = df.smiles.progress_map(featurize_with(featurizer))
        df["embeddings"] = df.features.dropna().progress_map(lambda f: model(f)[0])


def get_mat_embedder(config):
    return partial(
        process_huggingmolecules,
        model=StrippedMatModel.from_pretrained(config),
        featurizer=MatFeaturizer.from_pretrained(config)
    )


def get_grover_embedder(config):
    return partial(
        process_huggingmolecules,
        model=StrippedGroverModel.from_pretrained(config),
        featurizer=GroverFeaturizer.from_pretrained(config)
    )


def get_rmat_embedder(config):
    return partial(
        process_huggingmolecules,
        model=StrippedRMatModel.from_pretrained(config),
        featurizer=RMatFeaturizer.from_pretrained(config)
    )


def get_mol2vec_embedder():
    model = dc.feat.Mol2VecFingerprint("models/model_300dim.pkl")

    def process(smiles):
        with torch.no_grad():
            tqdm.pandas()
            smiles["embeddings"] = smiles.smiles.progress_map(lambda f: model(f)[0])

    return process


def get_embedder_names():
    return [
        "mat_masking_200k",
        "mat_masking_2M",
        "mat_masking_20M",
        "grover_base",
        'grover_large',
        "rmat_4M",
        "rmat_4M_rdkit",
        "mol2vec",
    ]


def get_embedder(name):
    if name in ["mat_masking_200k", "mat_masking_2M", "mat_masking_20M"]:
        return get_mat_embedder(name)
    elif name in ["grover_base", 'grover_large']:
        return get_grover_embedder(name)
    elif name in ["rmat_4M", "rmat_4M_rdkit"]:
        return get_rmat_embedder(name)
    elif name in ["mol2vec"]:
        return get_mol2vec_embedder()


if __name__ == "__main__":
    pass
