from utils import get_embedder_names, get_embedder
from datasets import get_dataset_names, get_dataset, get_tdc_names, get_ogb_names, get_ogb_regression_names, get_ogb_classification_names, get_tdc_regression_names, get_tdc_classification_names

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import linear_model
from sklearn.multioutput import ClassifierChain
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import mean_squared_error, f1_score
import matplotlib.pyplot as plt
from functools import partial
import os
import shelve
import tqdm
import click
import pickle
from tdc.benchmark_group import admet_group
from ogb.graphproppred import Evaluator

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeClassifierCV, RidgeCV
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_recall_curve, auc, roc_auc_score as roc_auc, make_scorer
from scipy.stats import spearmanr
import traceback


def predict_test(df, split_idx, model, **kwargs):
    scaler = StandardScaler()

    targets = list(filter(lambda col: col not in ['smiles', "features", 'embeddings', 'Drug_ID'], df.columns))

    train_val = pd.concat([df.loc[split_idx["train"]], df.loc[split_idx["valid"]]])
    train_val = train_val.fillna(train_val[targets].mode().iloc[0])

    X = np.vstack(train_val.embeddings.to_numpy())
    y = train_val[targets].to_numpy()

    clf = model(kwargs).fit(scaler.fit_transform(X), y)

    test = df.loc[split_idx["test"]]
    X = np.vstack(test.embeddings.to_numpy())

    return clf.predict(scaler.transform(X))


predict_regression_lin = partial(predict_test, model=lambda kwargs: linear_model.LinearRegression())

predict_regression_forest = partial(
    predict_test,
    model=lambda kwargs: GridSearchCV(
        RandomForestRegressor(
            n_estimators=100,
            n_jobs=-1,
            random_state=0,
        ),
        {
            "min_samples_split": np.logspace(1, 5, 4, base=2).astype(int)
        },
        n_jobs=-1,
        refit=True,
        scoring=kwargs.get("scoring", False),
    )
)

predict_regression_ridge = partial(
    predict_test,
    model=lambda kwargs: RidgeCV(
        alphas=np.logspace(-2, 2, 10),
        scoring=kwargs.get("scoring", False),
    )
)

predict_classification_lin = partial(predict_test, model=lambda kwargs: ClassifierChain(LogisticRegression()))


class RandomForestClassifierProba(RandomForestClassifier):
    def predict(self, X):
        return self.predict_proba(X)[:, 1]


predict_classification_forest = partial(
    predict_test,
    model=lambda kwargs: ClassifierChain(GridSearchCV(
        RandomForestClassifierProba(
            n_estimators=100,
            criterion="entropy",
            n_jobs=-1,
            random_state=0,
        ),
        {
            "min_samples_split": np.logspace(1, 5, 4, base=2).astype(int)
        },
        n_jobs=-1,
        refit=True,
        scoring=kwargs.get("scoring", False),
    )))

class RidgeClassifierCVProba(RidgeClassifierCV):
    def predict(self, X):
        return 1 / (1 + np.exp(-self.decision_function(X)))

predict_classification_ridge = partial(
    predict_test,
    model=lambda kwargs: ClassifierChain(
        RidgeClassifierCVProba(
            alphas=np.logspace(-2, 2, 10),
            class_weight="balanced",
            scoring=kwargs.get("scoring", False),
        )
    ))


def read(name):
    with open(f"results/{name}", "rb") as f:
        tmp = pickle.load(f)
    return tmp


def spearmancorr_score(x, y):
    rho, pval = spearmanr(x, y, axis=0)
    return rho * (-1)


def pr_auc_score(y_true, y_scores):
    try:
        precision, recall, _ = precision_recall_curve(y_true, y_scores)
        return auc(recall, precision)
    except ValueError:
        return 0


def roc_auc_score(y_true, y_scores):
    try:
        return roc_auc(y_true, y_scores)
    except ValueError:
        return 0


def get_metric(dataset):

    if dataset in [
        "BBB_Martins",
        "Bioavailability_Ma",
        "CYP3A4_Substrate_CarbonMangels",
        "HIA_Hou",
        "Pgp_Broccatelli",
        "ogbg-molbace",
        "ogbg-molbbbp",
        "ogbg-molclintox",
        "ogbg-molhiv",
        "ogbg-molsider",
        "ogbg-moltox21",
        "ogbg-moltoxcast"
    ]:
        return make_scorer(roc_auc_score), True
    elif dataset in [
        "CYP2C9_Substrate_CarbonMangels",
        "CYP2C9_Veith",
        "CYP2D6_Substrate_CarbonMangels",
        "CYP2D6_Veith",
        "CYP3A4_Veith",
    ]:
        return make_scorer(pr_auc_score), True
    elif dataset in [
        "Lipophilicity_AstraZeneca",
        "Solubility_AqSolDB",
    ]:
        return "neg_mean_absolute_error", False
    elif dataset in [
        "Caco2_Wang",
        "ogbg-molesol",
        "ogbg-molfreesolv",
        "ogbg-mollipo",
    ]:
        return "neg_root_mean_squared_error", False
    elif dataset in [
        "Clearance_Hepatocyte_AZ",
        "Half_Life_Obach",
        "VDss_Lombardo",
    ]:
        return make_scorer(spearmancorr_score), False
    elif dataset in [
        "ogbg-molmuv",
    ]:
        return "average_precision", True


def get_predict_fun(dataset_name, head_model):
    classification_names = get_tdc_classification_names() + get_ogb_classification_names()
    regression_names = get_tdc_regression_names() + get_ogb_regression_names()

    if dataset_name in classification_names and head_model == "linear":
        return predict_classification_lin
    elif dataset_name in classification_names and head_model == "forest":
        return predict_classification_forest
    elif dataset_name in classification_names and head_model == "ridge":
        return predict_classification_ridge
    elif dataset_name in regression_names and head_model == "linear":
        return predict_regression_lin
    elif dataset_name in regression_names and head_model == "forest":
        return predict_regression_forest
    elif dataset_name in regression_names and head_model == "ridge":
        return predict_regression_ridge


def evaluate_ogb(dataset_name, y_pred):
    evaluator = Evaluator(name=dataset_name)

    dataset, split_idx = get_dataset(dataset_name)
    targets = list(filter(lambda col: col not in ['smiles', "features", 'embeddings', 'Drug_ID'], dataset.columns))
    y_true = dataset.loc[split_idx["test"]][targets].to_numpy()

    input_dict = {"y_true": y_true.reshape((-1, len(targets))), "y_pred": y_pred.reshape((-1, len(targets)))}

    result_dict = evaluator.eval(input_dict)
    return list(result_dict.items())[0]


def evaluate_tdc(dataset_name, y_pred):
    group = admet_group(path='data/')
    benchmark = group.get(dataset_name)

    predictions = {}
    name = benchmark['name']
    a = benchmark["test"]

    predictions[name] = y_pred
    metric_name, metric_value = list(list(group.evaluate(predictions).values())[0].items())[0]
    return metric_name, metric_value


def evaluate(dataset_name, y_pred):
    if dataset_name in get_tdc_names():
        return evaluate_tdc(dataset_name, y_pred)
    elif dataset_name in get_ogb_names():
        return evaluate_ogb(dataset_name, y_pred)


def procedure(dataset_name, base_model, head_model):
    _, split_idx = get_dataset(dataset_name)

    df = pd.read_pickle(f"embeddings/{dataset_name}/{base_model}.zip").drop(["features"], axis=1, errors="ignore")

    predict_fun = get_predict_fun(dataset_name, head_model)

    scoring, predict_proba = get_metric(dataset_name)

    preds = predict_fun(df, split_idx, scoring=scoring, predict_proba=predict_proba)

    metric_name, metric_value = evaluate(dataset_name, preds)

    data = {
        'dataset': dataset_name,
        'base_model': base_model,
        'head_model': head_model,
        'metric': metric_name,
        'result': metric_value,
    }
    print(data)

    with open(f'results/{dataset_name}_{base_model}_{head_model}.pkl', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


@click.command()
@click.option("--dataset_name", required=True, type=str)
@click.option("--base_model", required=True, type=str)
@click.option("--head_model", required=True, type=str)
def main(dataset_name, base_model, head_model):
    try:
        procedure(dataset_name, base_model, head_model)
    except Exception as e:
        print(f"Exception while executing ({dataset_name}, {base_model}):\n{e}")
        traceback.print_exception(type(e), e, e.__traceback__)


if __name__ == "__main__":
    main()
