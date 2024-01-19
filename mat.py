import os
import random

import numpy as np
import torch
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils import compute_class_weight
from sklearn.utils.multiclass import unique_labels
from torch.nn import BCEWithLogitsLoss
from tqdm import tqdm

from MAT.src.featurization.data_utils import construct_loader, load_data_from_smiles
from MAT.src.transformer import make_model as make_mat_model


class MolecularAttentionTransformer(BaseEstimator, ClassifierMixin):
    def __init__(
        self,
        num_epochs: int = 1,
        batch_size: int = 1,
        learning_rate: float = 1e-5,
        weight_decay: float = 1e-5,
    ):
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay
        
        # ensure determinism
        os.environ["PYTHONHASHSEED"] = str(0)
        random.seed(0)
        np.random.seed(0)
        torch.manual_seed(0)
        torch.cuda.manual_seed_all(0)
        torch.use_deterministic_algorithms(True)

        model_params = {
            "d_atom": 28,
            "d_model": 1024,
            "N": 8,
            "h": 16,
            "N_dense": 1,
            "lambda_attention": 0.33,
            "lambda_distance": 0.33,
            "leaky_relu_slope": 0.1,
            "dense_output_nonlinearity": "relu",
            "distance_matrix_kernel": "exp",
            "dropout": 0.0,
            "aggregation_type": "mean",
        }
        self.model = make_mat_model(**model_params)
        pretrained_state_dict = torch.load("models/mat/pretrained_weights.pt")
        model_state_dict = self.model.state_dict()
        for name, param in pretrained_state_dict.items():
            if "generator" in name:
                continue
            if isinstance(param, torch.nn.Parameter):
                param = param.data
            model_state_dict[name].copy_(param)
            
        self.model.generator.proj = torch.nn.Identity()

    def predict(self, X: list[str]) -> np.ndarray:
        y = list(range(len(X)))
        X, y = load_data_from_smiles(X, y, one_hot_formal_charge=True)
        data_loader = construct_loader(X, y, batch_size=1, shuffle=False)

        results = []
        total = len(X) // self.batch_size
        for batch in tqdm(data_loader, total=total):
            with torch.no_grad():
                adjacency_matrix, node_features, distance_matrix, y = batch
                batch_mask = torch.sum(torch.abs(node_features), dim=-1) != 0
                output = self.model(
                    node_features, batch_mask, adjacency_matrix, distance_matrix, None
                )
                results.append(output)

        return results

if __name__ == "__main__":
    model = MolecularAttentionTransformer(0)
    print(model.predict(["CN1CC[C@]23C(=O)C[C@@H]4C(=CCO[C@H]5CC(=O)N(c6ccccc62)[C@@H]3[C@@H]54)C1"]))