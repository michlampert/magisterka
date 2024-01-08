import torch
from huggingmolecules import MatConfig, MatFeaturizer, MatModel
from huggingmolecules import GroverConfig, GroverFeaturizer, GroverModel
from huggingmolecules.featurization.featurization_grover import GroverBatchEncoding
from huggingmolecules import RMatConfig, RMatFeaturizer, RMatModel


class StrippedMatModel(MatModel):
    def __init__(self, config: MatConfig):
        super().__init__(config)
        self.generator.proj = torch.nn.Identity()

class StrippedGroverModel(GroverModel):
    def __init__(self, config: GroverConfig):
        super(StrippedGroverModel, self).__init__(config)
        self.mol_atom_from_atom_ffn = torch.nn.Identity()
        self.mol_atom_from_bond_ffn = torch.nn.Identity()

    def forward(self, batch: GroverBatchEncoding):
        atom_ffn_output, bond_ffn_output = super().forward(batch)
        return torch.cat([atom_ffn_output, bond_ffn_output], 1)

class StrippedRMatModel(RMatModel):
    def __init__(self, config: RMatConfig):
        super().__init__(config)
        self.generator.proj = torch.nn.Identity()


if __name__ == "__main__":
    config = RMatConfig.from_pretrained('rmat_4M')
    model = StrippedRMatModel(config)

    featurizer = RMatFeaturizer.from_pretrained('rmat_4M')
    batch = featurizer(['C/C=C/C', '[C]=O'])

    output = model(batch)
    print(output.size())
