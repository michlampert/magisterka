import pandas as pd
from tqdm import tqdm
import torch
import sys
import time
import datetime
from itertools import product
import os
import click
import logging

from huggingmolecules import MatConfig, MatFeaturizer, MatModel
from huggingmolecules import GroverConfig, GroverFeaturizer, GroverModel
from huggingmolecules import RMatConfig, RMatFeaturizer, RMatModel
from models import StrippedMatModel, StrippedGroverModel, StrippedRMatModel

from utils import get_embedder, get_embedder_names
from datasets import get_dataset_names, get_dataset

import rdkit.rdBase as rkrb
import rdkit.RDLogger as rkl

rkl.logger().setLevel(rkl.ERROR)
rkrb.DisableLog('rdApp.error')

logger = logging.getLogger("molecules")
logger.setLevel(logging.INFO)

fh = logging.FileHandler('logs.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


def procedure(dataset_name, df, model_name, model, *, max_samples=None):

    if not os.path.exists("embeddings"):
        os.mkdir("embeddings")

    if not os.path.exists(f"embeddings/{dataset_name}"):
        os.mkdir(f"embeddings/{dataset_name}")

    logger.info(f"Processing {dataset_name} with {model_name}")

    if os.path.isfile(f"embeddings/{dataset_name}/{model_name}.zip"):
        logger.info("✔️")
        return

    if max_samples:
        df = df.sample(n=max_samples)

    start = time.time()

    model(df)

    df.to_pickle(f'embeddings/{dataset_name}/{model_name}.zip')

    logger.info(f"Processing {dataset_name} with {model_name} took {((time.time() - start)/60):.1f}m")


@click.command()
@click.option("--model_name", required=True, type=str)
@click.option("--dataset_name", required=True, type=str)
@click.option("--max_samples", default=None, type=int)
def main(model_name, dataset_name, max_samples):

    load_graphs = model_name in ["Graphormer"]
    df, _ = get_dataset(dataset_name, load_graphs)

    model = get_embedder(model_name)

    procedure(dataset_name, df, model_name, model, max_samples=max_samples)


if __name__ == "__main__":
    main()
