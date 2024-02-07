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
from tdc.single_pred import ADME


def load_ogb_dataset(name: str):
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
        pd.concat([train, valid, test]).rename(columns={"Drug": "smiles"}).drop(["Drug_ID"], axis=1, errors='ignore'),
        {"train": train_range, "valid": valid_range, "test": test_range}
    )

def get_ogb_names():
    return [
        "ogbg-molbace",
        "ogbg-moltox21",
        "ogbg-molbbbp",
        "ogbg-molclintox",
        "ogbg-molmuv",
        "ogbg-molsider",
        "ogbg-moltoxcast",
        "ogbg-molesol",
        "ogbg-molfreesolv",
        "ogbg-mollipo"
    ]

def get_tdc_names():
    return [
        'Caco2_Wang',
        'Half_Life_Obach',
        'PAMPA_NCATS',
        'HIA_Hou',
        'Pgp_Broccatelli',
        'Bioavailability_Ma',
        'Lipophilicity_AstraZeneca',
        'Solubility_AqSolDB',
        'HydrationFreeEnergy_FreeSolv',
        'BBB_Martins',
        'PPBR_AZ',
        'VDss_Lombardo',
        'CYP2C19_Veith',
        'CYP2D6_Veith',
        'CYP3A4_Veith',
        'CYP1A2_Veith',
        'CYP2C9_Veith',
        'CYP2C9_Substrate_CarbonMangels',
        'CYP2D6_Substrate_CarbonMangels',
        'CYP3A4_Substrate_CarbonMangels',
        'Clearance_Hepatocyte_AZ',
    ]

def get_dataset_names() -> Iterator:
    return chain(
        get_ogb_names(),
        get_tdc_names(),
    )

def get_dataset(name):
    if name in get_ogb_names():
        return load_ogb_dataset(name)
    elif name in get_tdc_names():
        return load_tdc_dataset(ADME, name)