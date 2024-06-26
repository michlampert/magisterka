import pandas as pd
import logging
import time
from models import *
from typing import Iterator, Callable, Tuple
from tqdm import tqdm
import deepchem as dc
from rdkit import Chem
from itertools import chain
from functools import partial
from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch.nn as nn
from molbert.utils.featurizer.molbert_featurizer import MolBertFeaturizer

from transformers.models.graphormer.collating_graphormer import preprocess_item, GraphormerDataCollator
from transformers import GraphormerForGraphClassification
from pretrain_gnns.chem.model import GNN_graphpred
from pretrain_gnns.chem.loader import mol_to_graph_data_obj_simple

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


def get_chemberta_embedder(config):
    chemberta = AutoModelForMaskedLM.from_pretrained(f"DeepChem/{config}")
    chemberta._modules["lm_head"] = nn.Identity()
    tokenizer = AutoTokenizer.from_pretrained(f"DeepChem/{config}")

    def model(smiles):
        encoded_input = tokenizer(smiles, return_tensors="pt", padding=True, truncation=True)
        model_output = chemberta(**encoded_input)
        return model_output[0][::, 0, ::]

    def process(df):
        with torch.no_grad():
            tqdm.pandas()
            df["embeddings"] = df.smiles.progress_map(lambda f: model(f)[0])

    return process


def get_molbert_embedder():
    path_to_checkpoint = './models/molbert_100epochs/molbert_100epochs/checkpoints/last.ckpt'
    model = MolBertFeaturizer(path_to_checkpoint, device="cpu")

    def process(df):
        with torch.no_grad():
            tqdm.pandas()
            df["embeddings"] = df.smiles.progress_map(lambda f: model.transform(f)[0][0])

    return process


def get_graphormer_embedder():
    model_checkpoint = "clefourrier/graphormer-base-pcqm4mv2"
    model = GraphormerForGraphClassification.from_pretrained(model_checkpoint)
    model.classifier = torch.nn.Identity()

    def preprocess(molecules):
        result = GraphormerDataCollator()([{**preprocess_item(molecule)} for molecule in molecules])
        result["labels"] = None
        return result
    
    def inner(molecule):
        try:
            return model.forward(**preprocess([molecule])).logits.flatten()
        except IndexError:
            logger.warning(f"\rInvalid molecule" + " " * 20)
            return None
    
    def process(df):
        with torch.no_grad():
            tqdm.pandas()
            df["embeddings"] = df.graph.progress_map(inner)

    return process

def get_transformerm_embedder():
    model = GNN_graphpred(5, 300, 1)
    model.from_pretrained("pretrain_gnns/chem/model_gin/supervised_masking.pth")
    model.graph_pred_linear = torch.nn.Identity()
    model
    
    def inner(molecule):
        try:
            g = mol_to_graph_data_obj_simple(Chem.MolFromSmiles(molecule))
            g.id = torch.tensor([0])
            g.y = torch.tensor([0])
            return model(g).flatten()
        except:
            logger.warning(f"\rInvalid molecule {molecule}" + " " * 20)
            return None
    
    def process(df):
        with torch.no_grad():
            tqdm.pandas()
            df["embeddings"] = df.smiles.progress_map(inner)
    
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
        "ChemBERTa-5M-MTR",
        "ChemBERTa-10M-MTR",
        "ChemBERTa-77M-MTR",
        'molbert',
        "SELFormer",
        "Graphormer",
        "Transformer-M",
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
    elif name in ["ChemBERTa-5M-MTR", "ChemBERTa-10M-MTR", "ChemBERTa-77M-MTR"]:
        return get_chemberta_embedder(name)
    elif name in ['molbert']:
        return get_molbert_embedder()
    elif name in ['Graphormer']:
        return get_graphormer_embedder()
    elif name in ['Transformer-M']:
        return get_transformerm_embedder()


if __name__ == "__main__":
    pass
