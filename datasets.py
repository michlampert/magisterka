import pandas as pd
import numpy as np
from ogb.graphproppred import PygGraphPropPredDataset
import logging
import time
from models import *
from typing import Iterator, Callable, Tuple
from tqdm import tqdm
import deepchem as dc
from rdkit import Chem
from itertools import chain
from tdc.single_pred import ADME
from tdc.benchmark_group import admet_group
from tdc.chem_utils import MolConvert
from ogb.utils import smiles2graph


def load_ogb_dataset(name: str, load_graphs = False):
    dataset = PygGraphPropPredDataset(name=name)

    smiles = pd.read_csv(f"dataset/{name.replace('-', '_')}/mapping/mol.csv.gz").drop(['mol_id'], axis=1)
    if load_graphs: smiles["graph"] = list(dataset)
    return smiles, dataset.get_idx_split()


def load_tdc_dataset(module, name: str, load_graphs = False):
    data = module(name=name)
    split = data.get_split()

    train, valid, test = split["train"], split["valid"], split["test"]

    dataset = pd.concat([train, valid, test]).reset_index(drop=True)
    
    if load_graphs:
        converter = MolConvert(src = 'SMILES', dst = 'PyG')
        dataset["graph"] = dataset["Drug"].map(lambda smiles: {**smiles2graph(smiles), "x": converter(smiles).x, "y": np.array([[0]])})
    
    group = admet_group(path = 'data/')
    benchmark = group.get(name)
    
    return (
        dataset.rename(columns={"Drug": "smiles"}).drop(["Drug_ID"], axis=1, errors='ignore'),
        {
            "train": list(benchmark["train_val"].merge(dataset.reset_index().groupby(["Drug_ID", "Drug"]).first(), on=["Drug_ID", "Drug"])["index"]),
            "valid": [],
            "test": list(benchmark["test"].merge(dataset.reset_index().groupby(["Drug_ID", "Drug"]).first(), on=["Drug_ID", "Drug"])["index"])}
    )


def get_ogb_regression_names():
    return [
        "ogbg-molesol",
        "ogbg-molfreesolv",
        "ogbg-mollipo",
    ]


def get_ogb_classification_names():
    return [
        "ogbg-molbace",
        "ogbg-molbbbp",
        "ogbg-molclintox",
        "ogbg-molsider",
        "ogbg-moltox21",
        "ogbg-moltoxcast",
        "ogbg-molmuv",
        "ogbg-molhiv",
    ]


def get_ogb_names():
    return get_ogb_regression_names() + get_ogb_classification_names()


def get_tdc_regression_names():
    return [
        'Caco2_Wang',
        'Half_Life_Obach',
        'Lipophilicity_AstraZeneca',
        'Solubility_AqSolDB',
        # 'HydrationFreeEnergy_FreeSolv',
        # 'PPBR_AZ',
        'VDss_Lombardo',
        'Clearance_Hepatocyte_AZ',
    ]


def get_tdc_classification_names():
    return [
        # "PAMPA_NCATS",
        "HIA_Hou",
        "Pgp_Broccatelli",
        "Bioavailability_Ma",
        "BBB_Martins",
        # "CYP2C19_Veith",
        "CYP2D6_Veith",
        "CYP3A4_Veith",
        # "CYP1A2_Veith",
        "CYP2C9_Veith",
        "CYP2C9_Substrate_CarbonMangels",
        "CYP2D6_Substrate_CarbonMangels",
        "CYP3A4_Substrate_CarbonMangels",
    ]


def get_tdc_names():
    return get_tdc_regression_names() + get_tdc_classification_names()

def get_regression_names():
    return get_ogb_regression_names() + get_tdc_regression_names()

def get_classification_names():
    return get_ogb_classification_names() + get_tdc_classification_names()


def get_dataset_names() -> Iterator:
    return chain(
        get_ogb_names(),
        get_tdc_names(),
    )


def get_dataset(name, load_graphs = False):
    if name in get_ogb_names():
        return load_ogb_dataset(name, load_graphs)
    elif name in get_tdc_names():
        return load_tdc_dataset(ADME, name, load_graphs)
