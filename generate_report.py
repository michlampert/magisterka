
import os
import pickle
import pandas as pd
from datasets import *

ascending = {
    "roc-auc": False,
    "rocauc": False,
    "pr-auc": False,
    "mae": True,
    "rmse": True,
    "spearman": False,
    "ap": False,
}

sota_results = list(map(
    lambda d: {**d, 'base_model': '**SOTA**', 'head_model': "-"},
    [
        {'dataset': 'ogbg-molhiv', 'metric': 'rocauc', 'result': 0.8475},
        {'dataset': 'BBB_Martins', 'metric': 'roc-auc', 'result': 0.920},
        {'dataset': 'Bioavailability_Ma', 'metric': 'rocauc', 'result': 0.748},
        {'dataset': 'CYP2C9_Substrate_CarbonMangels', 'metric': 'pr-auc', 'result': 0.441},
        {'dataset': 'CYP2C9_Veith', 'metric': 'pr-auc', 'result': 0.859},
        {'dataset': 'CYP2D6_Substrate_CarbonMangels', 'metric': 'pr-auc', 'result': 0.736},
        {'dataset': 'CYP2D6_Veith', 'metric': 'pr-auc', 'result': 0.790},
        {'dataset': 'CYP3A4_Substrate_CarbonMangels', 'metric': 'roc-auc', 'result': 0.667},
        {'dataset': 'CYP3A4_Veith', 'metric': 'pr-auc', 'result': 0.916},
        {'dataset': 'Caco2_Wang', 'metric': 'mae', 'result': 0.276},
        {'dataset': 'Clearance_Hepatocyte_AZ', 'metric': 'spearman', 'result': 0.536},
        {'dataset': 'HIA_Hou', 'metric': 'roc-auc', 'result': 0.989},
        {'dataset': 'Half_Life_Obach', 'metric': 'spearman', 'result': 0.576},
        {'dataset': 'Lipophilicity_AstraZeneca', 'metric': 'mae', 'result': 0.467},
        {'dataset': 'Pgp_Broccatelli', 'metric': 'roc-auc', 'result': 0.938},
        {'dataset': 'Solubility_AqSolDB', 'metric': 'mae', 'result': 0.761},
        {'dataset': 'VDss_Lombardo', 'metric': 'spearman', 'result': 0.713},
    ]
))


def write_to_file(content):
    with open("results.md", "a") as f:
        f.write(content)
        f.write("\n\n")


def read(name):
    with open(f"results/{name}", "rb") as f:
        return pickle.load(f)


def main():
    with open("results.md", "w"):
        pass

    results = pd.DataFrame.from_records([read(name) for name in os.listdir("results/")] + sota_results)

    for name, group in results.groupby("dataset"):
        write_to_file(f"### {name} ({'classification' if name in [*get_tdc_classification_names(), *get_ogb_classification_names()] else 'regression'})")
        metric_name = list(group.metric)[0]
        write_to_file(group.sort_values("result", ascending=ascending[metric_name]).to_markdown(index=False))


if __name__ == "__main__":
    main()
