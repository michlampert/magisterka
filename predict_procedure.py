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



def predict_test(df, split_idx, model):
    targets = list(filter(lambda col: col not in ['smiles', "features", 'embeddings', 'Drug_ID'], df.columns))
    
    train_val = pd.concat([df.loc[split_idx["train"]], df.loc[split_idx["valid"]]])
    train_val = train_val.fillna(train_val[targets].mode().iloc[0])
    
    X = np.vstack(train_val.embeddings.to_numpy())
    y = train_val[targets].to_numpy()
    
    clf = model().fit(X, y)
    
    test = df.loc[split_idx["test"]]
    X = np.vstack(test.embeddings.to_numpy())
    
    return clf.predict(X)

predict_regression_lin = partial(predict_test, model=lambda: linear_model.LinearRegression())
predict_regression_forest = partial(predict_test, model=lambda: RandomForestRegressor(n_estimators=10, min_samples_split=10))

predict_classification_lin = partial(predict_test, model=lambda: ClassifierChain(LogisticRegression()))
predict_classification_forest = partial(predict_test, model=lambda: ClassifierChain(RandomForestClassifier(n_estimators=10, min_samples_split=10)))

def get_predict_fun(dataset_name, head_model):
    classification_names = get_tdc_classification_names() + get_ogb_classification_names()
    regression_names = get_tdc_regression_names() + get_ogb_regression_names()
    
    if dataset_name in classification_names and head_model == "linear":
        return predict_classification_lin
    elif dataset_name in classification_names and head_model == "forest":
        return predict_classification_forest
    elif dataset_name in regression_names and head_model == "linear":
        return predict_regression_lin
    elif dataset_name in regression_names and head_model == "forest":
        return predict_regression_forest

def evaluate_ogb(dataset_name, y_pred):
    evaluator = Evaluator(name = dataset_name)
    
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

def procedure(dataset_name, base_model):
    if os.path.isfile(f"embeddings/{dataset_name}/{base_model}.zip"):
        for head_model in ["linear", "forest"]:

            _, split_idx = get_dataset(dataset_name)
            df = pd.read_pickle(f"embeddings/{dataset_name}/{base_model}.zip")

            predict_fun = get_predict_fun(dataset_name, head_model)

            preds = predict_fun(df, split_idx)

            metric_name, metric_value = evaluate(dataset_name, preds)

            with open(f'results/{dataset_name}_{base_model}_{head_model}.pkl', 'wb') as f:
                data = {
                    'dataset': dataset_name,
                    'base_model': base_model,
                    'head_model': head_model,
                    'metric': metric_name,
                    'result': metric_value
                }
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


@click.command()
@click.option("--dataset_name", required=True, type=str)
@click.option("--base_model", required=True, type=str)
def main(dataset_name, base_model):
    try:
        procedure(dataset_name, base_model)
    except Exception as e:
        print(f"Exception while executing ({dataset_name}, {base_model}):\n{e}")
    
if __name__ == "__main__":
    main()