### BBB_Martins (classification)

| dataset     | base_model        | head_model   | metric   |   result |
|:------------|:------------------|:-------------|:---------|---------:|
| BBB_Martins | **SOTA**          | -            | roc-auc  |    0.92  |
| BBB_Martins | rmat_4M_rdkit     | forest       | roc-auc  |    0.91  |
| BBB_Martins | rmat_4M           | forest       | roc-auc  |    0.908 |
| BBB_Martins | mol2vec           | forest       | roc-auc  |    0.906 |
| BBB_Martins | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.903 |
| BBB_Martins | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.897 |
| BBB_Martins | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.894 |
| BBB_Martins | mat_masking_20M   | forest       | roc-auc  |    0.879 |
| BBB_Martins | mat_masking_2M    | forest       | roc-auc  |    0.875 |
| BBB_Martins | mat_masking_200k  | forest       | roc-auc  |    0.874 |
| BBB_Martins | ChemBERTa-77M-MTR | ridge        | roc-auc  |    0.864 |
| BBB_Martins | mol2vec           | ridge        | roc-auc  |    0.864 |
| BBB_Martins | ChemBERTa-5M-MTR  | ridge        | roc-auc  |    0.846 |
| BBB_Martins | ChemBERTa-10M-MTR | ridge        | roc-auc  |    0.838 |
| BBB_Martins | mat_masking_200k  | linear       | roc-auc  |    0.816 |
| BBB_Martins | mol2vec           | linear       | roc-auc  |    0.807 |
| BBB_Martins | rmat_4M_rdkit     | linear       | roc-auc  |    0.784 |
| BBB_Martins | mat_masking_2M    | linear       | roc-auc  |    0.784 |
| BBB_Martins | rmat_4M           | linear       | roc-auc  |    0.78  |
| BBB_Martins | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.778 |
| BBB_Martins | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.777 |
| BBB_Martins | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.774 |
| BBB_Martins | mat_masking_20M   | linear       | roc-auc  |    0.772 |
| BBB_Martins | mat_masking_200k  | ridge        | roc-auc  |    0.757 |
| BBB_Martins | rmat_4M_rdkit     | ridge        | roc-auc  |    0.712 |
| BBB_Martins | grover_large      | forest       | roc-auc  |    0.705 |
| BBB_Martins | grover_base       | linear       | roc-auc  |    0.692 |
| BBB_Martins | grover_large      | ridge        | roc-auc  |    0.671 |
| BBB_Martins | grover_large      | linear       | roc-auc  |    0.67  |
| BBB_Martins | grover_base       | forest       | roc-auc  |    0.662 |
| BBB_Martins | rmat_4M           | ridge        | roc-auc  |    0.656 |
| BBB_Martins | mat_masking_2M    | ridge        | roc-auc  |    0.65  |
| BBB_Martins | grover_base       | ridge        | roc-auc  |    0.635 |
| BBB_Martins | mat_masking_20M   | ridge        | roc-auc  |    0.628 |
| BBB_Martins | molbert           | forest       | roc-auc  |    0.551 |

### Bioavailability_Ma (classification)

| dataset            | base_model        | head_model   | metric   |   result |
|:-------------------|:------------------|:-------------|:---------|---------:|
| Bioavailability_Ma | **SOTA**          | -            | rocauc   |    0.748 |
| Bioavailability_Ma | rmat_4M           | forest       | roc-auc  |    0.733 |
| Bioavailability_Ma | mol2vec           | forest       | roc-auc  |    0.728 |
| Bioavailability_Ma | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.719 |
| Bioavailability_Ma | rmat_4M_rdkit     | forest       | roc-auc  |    0.714 |
| Bioavailability_Ma | rmat_4M_rdkit     | ridge        | roc-auc  |    0.713 |
| Bioavailability_Ma | mat_masking_2M    | forest       | roc-auc  |    0.707 |
| Bioavailability_Ma | ChemBERTa-5M-MTR  | ridge        | roc-auc  |    0.684 |
| Bioavailability_Ma | mat_masking_200k  | forest       | roc-auc  |    0.684 |
| Bioavailability_Ma | mat_masking_20M   | forest       | roc-auc  |    0.682 |
| Bioavailability_Ma | rmat_4M           | ridge        | roc-auc  |    0.673 |
| Bioavailability_Ma | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.663 |
| Bioavailability_Ma | ChemBERTa-77M-MTR | ridge        | roc-auc  |    0.66  |
| Bioavailability_Ma | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.636 |
| Bioavailability_Ma | rmat_4M           | linear       | roc-auc  |    0.627 |
| Bioavailability_Ma | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.62  |
| Bioavailability_Ma | rmat_4M_rdkit     | linear       | roc-auc  |    0.616 |
| Bioavailability_Ma | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.605 |
| Bioavailability_Ma | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.605 |
| Bioavailability_Ma | ChemBERTa-10M-MTR | ridge        | roc-auc  |    0.597 |
| Bioavailability_Ma | mol2vec           | linear       | roc-auc  |    0.596 |
| Bioavailability_Ma | mat_masking_2M    | linear       | roc-auc  |    0.593 |
| Bioavailability_Ma | mat_masking_2M    | ridge        | roc-auc  |    0.589 |
| Bioavailability_Ma | mol2vec           | ridge        | roc-auc  |    0.576 |
| Bioavailability_Ma | mat_masking_200k  | ridge        | roc-auc  |    0.565 |
| Bioavailability_Ma | mat_masking_200k  | linear       | roc-auc  |    0.534 |
| Bioavailability_Ma | molbert           | forest       | roc-auc  |    0.533 |
| Bioavailability_Ma | grover_large      | forest       | roc-auc  |    0.521 |
| Bioavailability_Ma | mat_masking_20M   | linear       | roc-auc  |    0.508 |
| Bioavailability_Ma | grover_large      | linear       | roc-auc  |    0.499 |
| Bioavailability_Ma | mat_masking_20M   | ridge        | roc-auc  |    0.495 |
| Bioavailability_Ma | grover_base       | forest       | roc-auc  |    0.493 |
| Bioavailability_Ma | grover_large      | ridge        | roc-auc  |    0.487 |
| Bioavailability_Ma | grover_base       | ridge        | roc-auc  |    0.419 |
| Bioavailability_Ma | grover_base       | linear       | roc-auc  |    0.408 |

### CYP2C9_Substrate_CarbonMangels (classification)

| dataset                        | base_model        | head_model   | metric   |   result |
|:-------------------------------|:------------------|:-------------|:---------|---------:|
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.462 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.451 |
| CYP2C9_Substrate_CarbonMangels | **SOTA**          | -            | pr-auc   |    0.441 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.433 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M           | forest       | pr-auc   |    0.426 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M_rdkit     | forest       | pr-auc   |    0.423 |
| CYP2C9_Substrate_CarbonMangels | grover_large      | forest       | pr-auc   |    0.397 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_20M   | forest       | pr-auc   |    0.378 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_200k  | forest       | pr-auc   |    0.378 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_2M    | forest       | pr-auc   |    0.373 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.372 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M           | ridge        | pr-auc   |    0.35  |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-10M-MTR | ridge        | pr-auc   |    0.35  |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.347 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_200k  | ridge        | pr-auc   |    0.344 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | ridge        | pr-auc   |    0.34  |
| CYP2C9_Substrate_CarbonMangels | mol2vec           | forest       | pr-auc   |    0.339 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.337 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-77M-MTR | ridge        | pr-auc   |    0.333 |
| CYP2C9_Substrate_CarbonMangels | grover_large      | ridge        | pr-auc   |    0.329 |
| CYP2C9_Substrate_CarbonMangels | grover_large      | linear       | pr-auc   |    0.327 |
| CYP2C9_Substrate_CarbonMangels | mol2vec           | ridge        | pr-auc   |    0.317 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M_rdkit     | ridge        | pr-auc   |    0.316 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_20M   | ridge        | pr-auc   |    0.297 |
| CYP2C9_Substrate_CarbonMangels | mol2vec           | linear       | pr-auc   |    0.283 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_2M    | linear       | pr-auc   |    0.282 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_20M   | linear       | pr-auc   |    0.282 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_200k  | linear       | pr-auc   |    0.281 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M           | linear       | pr-auc   |    0.28  |
| CYP2C9_Substrate_CarbonMangels | rmat_4M_rdkit     | linear       | pr-auc   |    0.277 |
| CYP2C9_Substrate_CarbonMangels | grover_base       | linear       | pr-auc   |    0.271 |
| CYP2C9_Substrate_CarbonMangels | grover_base       | forest       | pr-auc   |    0.271 |
| CYP2C9_Substrate_CarbonMangels | molbert           | forest       | pr-auc   |    0.263 |
| CYP2C9_Substrate_CarbonMangels | grover_base       | ridge        | pr-auc   |    0.254 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_2M    | ridge        | pr-auc   |    0.239 |

### CYP2C9_Veith (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| CYP2C9_Veith | **SOTA**          | -            | pr-auc   |    0.859 |
| CYP2C9_Veith | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.756 |
| CYP2C9_Veith | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.749 |
| CYP2C9_Veith | rmat_4M_rdkit     | forest       | pr-auc   |    0.748 |
| CYP2C9_Veith | rmat_4M           | forest       | pr-auc   |    0.747 |
| CYP2C9_Veith | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.746 |
| CYP2C9_Veith | mat_masking_2M    | forest       | pr-auc   |    0.745 |
| CYP2C9_Veith | mat_masking_20M   | forest       | pr-auc   |    0.734 |
| CYP2C9_Veith | mat_masking_200k  | forest       | pr-auc   |    0.727 |
| CYP2C9_Veith | ChemBERTa-77M-MTR | ridge        | pr-auc   |    0.724 |
| CYP2C9_Veith | mol2vec           | forest       | pr-auc   |    0.712 |
| CYP2C9_Veith | ChemBERTa-5M-MTR  | ridge        | pr-auc   |    0.707 |
| CYP2C9_Veith | mat_masking_200k  | ridge        | pr-auc   |    0.696 |
| CYP2C9_Veith | mat_masking_2M    | ridge        | pr-auc   |    0.693 |
| CYP2C9_Veith | ChemBERTa-10M-MTR | ridge        | pr-auc   |    0.691 |
| CYP2C9_Veith | mol2vec           | ridge        | pr-auc   |    0.679 |
| CYP2C9_Veith | mat_masking_20M   | ridge        | pr-auc   |    0.669 |
| CYP2C9_Veith | rmat_4M_rdkit     | ridge        | pr-auc   |    0.641 |
| CYP2C9_Veith | rmat_4M           | ridge        | pr-auc   |    0.614 |
| CYP2C9_Veith | grover_base       | ridge        | pr-auc   |    0.602 |
| CYP2C9_Veith | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.582 |
| CYP2C9_Veith | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.579 |
| CYP2C9_Veith | rmat_4M           | linear       | pr-auc   |    0.574 |
| CYP2C9_Veith | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.573 |
| CYP2C9_Veith | grover_large      | ridge        | pr-auc   |    0.573 |
| CYP2C9_Veith | mat_masking_2M    | linear       | pr-auc   |    0.572 |
| CYP2C9_Veith | mat_masking_200k  | linear       | pr-auc   |    0.56  |
| CYP2C9_Veith | rmat_4M_rdkit     | linear       | pr-auc   |    0.559 |
| CYP2C9_Veith | grover_large      | forest       | pr-auc   |    0.558 |
| CYP2C9_Veith | mat_masking_20M   | linear       | pr-auc   |    0.552 |
| CYP2C9_Veith | grover_base       | forest       | pr-auc   |    0.548 |
| CYP2C9_Veith | mol2vec           | linear       | pr-auc   |    0.529 |
| CYP2C9_Veith | grover_large      | linear       | pr-auc   |    0.497 |
| CYP2C9_Veith | grover_base       | linear       | pr-auc   |    0.493 |

### CYP2D6_Substrate_CarbonMangels (classification)

| dataset                        | base_model        | head_model   | metric   |   result |
|:-------------------------------|:------------------|:-------------|:---------|---------:|
| CYP2D6_Substrate_CarbonMangels | **SOTA**          | -            | pr-auc   |    0.736 |
| CYP2D6_Substrate_CarbonMangels | mol2vec           | forest       | pr-auc   |    0.703 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.699 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.698 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_2M    | forest       | pr-auc   |    0.691 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M_rdkit     | forest       | pr-auc   |    0.684 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_20M   | forest       | pr-auc   |    0.672 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M           | forest       | pr-auc   |    0.654 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.649 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_200k  | forest       | pr-auc   |    0.615 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_20M   | ridge        | pr-auc   |    0.586 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M_rdkit     | ridge        | pr-auc   |    0.57  |
| CYP2D6_Substrate_CarbonMangels | rmat_4M           | ridge        | pr-auc   |    0.557 |
| CYP2D6_Substrate_CarbonMangels | grover_large      | forest       | pr-auc   |    0.547 |
| CYP2D6_Substrate_CarbonMangels | grover_base       | forest       | pr-auc   |    0.546 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_200k  | linear       | pr-auc   |    0.526 |
| CYP2D6_Substrate_CarbonMangels | mol2vec           | ridge        | pr-auc   |    0.515 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-77M-MTR | ridge        | pr-auc   |    0.502 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.5   |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.493 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_20M   | linear       | pr-auc   |    0.487 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.487 |
| CYP2D6_Substrate_CarbonMangels | mol2vec           | linear       | pr-auc   |    0.483 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M_rdkit     | linear       | pr-auc   |    0.481 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M           | linear       | pr-auc   |    0.481 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_200k  | ridge        | pr-auc   |    0.474 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_2M    | ridge        | pr-auc   |    0.47  |
| CYP2D6_Substrate_CarbonMangels | mat_masking_2M    | linear       | pr-auc   |    0.46  |
| CYP2D6_Substrate_CarbonMangels | grover_base       | ridge        | pr-auc   |    0.457 |
| CYP2D6_Substrate_CarbonMangels | grover_large      | ridge        | pr-auc   |    0.434 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | ridge        | pr-auc   |    0.423 |
| CYP2D6_Substrate_CarbonMangels | grover_large      | linear       | pr-auc   |    0.407 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-10M-MTR | ridge        | pr-auc   |    0.398 |
| CYP2D6_Substrate_CarbonMangels | grover_base       | linear       | pr-auc   |    0.383 |
| CYP2D6_Substrate_CarbonMangels | molbert           | forest       | pr-auc   |    0.318 |

### CYP2D6_Veith (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| CYP2D6_Veith | **SOTA**          | -            | pr-auc   |    0.79  |
| CYP2D6_Veith | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.652 |
| CYP2D6_Veith | rmat_4M_rdkit     | forest       | pr-auc   |    0.652 |
| CYP2D6_Veith | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.644 |
| CYP2D6_Veith | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.634 |
| CYP2D6_Veith | mat_masking_2M    | forest       | pr-auc   |    0.624 |
| CYP2D6_Veith | mat_masking_20M   | forest       | pr-auc   |    0.62  |
| CYP2D6_Veith | mat_masking_200k  | forest       | pr-auc   |    0.604 |
| CYP2D6_Veith | mol2vec           | forest       | pr-auc   |    0.597 |
| CYP2D6_Veith | ChemBERTa-10M-MTR | ridge        | pr-auc   |    0.583 |
| CYP2D6_Veith | ChemBERTa-5M-MTR  | ridge        | pr-auc   |    0.561 |
| CYP2D6_Veith | ChemBERTa-77M-MTR | ridge        | pr-auc   |    0.553 |
| CYP2D6_Veith | mol2vec           | ridge        | pr-auc   |    0.551 |
| CYP2D6_Veith | mat_masking_200k  | ridge        | pr-auc   |    0.544 |
| CYP2D6_Veith | mat_masking_2M    | ridge        | pr-auc   |    0.533 |
| CYP2D6_Veith | mat_masking_20M   | ridge        | pr-auc   |    0.528 |
| CYP2D6_Veith | rmat_4M_rdkit     | ridge        | pr-auc   |    0.427 |
| CYP2D6_Veith | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.42  |
| CYP2D6_Veith | grover_base       | ridge        | pr-auc   |    0.419 |
| CYP2D6_Veith | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.405 |
| CYP2D6_Veith | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.397 |
| CYP2D6_Veith | mat_masking_200k  | linear       | pr-auc   |    0.393 |
| CYP2D6_Veith | rmat_4M_rdkit     | linear       | pr-auc   |    0.384 |
| CYP2D6_Veith | grover_large      | ridge        | pr-auc   |    0.374 |
| CYP2D6_Veith | mol2vec           | linear       | pr-auc   |    0.367 |
| CYP2D6_Veith | mat_masking_2M    | linear       | pr-auc   |    0.365 |
| CYP2D6_Veith | grover_base       | forest       | pr-auc   |    0.363 |
| CYP2D6_Veith | grover_large      | forest       | pr-auc   |    0.36  |
| CYP2D6_Veith | mat_masking_20M   | linear       | pr-auc   |    0.354 |
| CYP2D6_Veith | grover_base       | linear       | pr-auc   |    0.299 |
| CYP2D6_Veith | grover_large      | linear       | pr-auc   |    0.282 |

### CYP3A4_Substrate_CarbonMangels (classification)

| dataset                        | base_model        | head_model   | metric   |   result |
|:-------------------------------|:------------------|:-------------|:---------|---------:|
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.696 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.673 |
| CYP3A4_Substrate_CarbonMangels | **SOTA**          | -            | roc-auc  |    0.667 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-77M-MTR | ridge        | roc-auc  |    0.656 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_200k  | forest       | roc-auc  |    0.647 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.646 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_2M    | forest       | roc-auc  |    0.646 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M           | forest       | roc-auc  |    0.643 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_20M   | forest       | roc-auc  |    0.635 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_20M   | ridge        | roc-auc  |    0.634 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.634 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.631 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M_rdkit     | forest       | roc-auc  |    0.63  |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.63  |
| CYP3A4_Substrate_CarbonMangels | mol2vec           | linear       | roc-auc  |    0.624 |
| CYP3A4_Substrate_CarbonMangels | mol2vec           | forest       | roc-auc  |    0.624 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M_rdkit     | ridge        | roc-auc  |    0.62  |
| CYP3A4_Substrate_CarbonMangels | mat_masking_2M    | linear       | roc-auc  |    0.616 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_20M   | linear       | roc-auc  |    0.613 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_2M    | ridge        | roc-auc  |    0.607 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_200k  | linear       | roc-auc  |    0.604 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-10M-MTR | ridge        | roc-auc  |    0.591 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | ridge        | roc-auc  |    0.587 |
| CYP3A4_Substrate_CarbonMangels | grover_base       | linear       | roc-auc  |    0.582 |
| CYP3A4_Substrate_CarbonMangels | mol2vec           | ridge        | roc-auc  |    0.567 |
| CYP3A4_Substrate_CarbonMangels | grover_large      | ridge        | roc-auc  |    0.565 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M           | linear       | roc-auc  |    0.564 |
| CYP3A4_Substrate_CarbonMangels | grover_base       | ridge        | roc-auc  |    0.556 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M           | ridge        | roc-auc  |    0.543 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_200k  | ridge        | roc-auc  |    0.543 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M_rdkit     | linear       | roc-auc  |    0.541 |
| CYP3A4_Substrate_CarbonMangels | grover_large      | linear       | roc-auc  |    0.536 |
| CYP3A4_Substrate_CarbonMangels | grover_base       | forest       | roc-auc  |    0.518 |
| CYP3A4_Substrate_CarbonMangels | molbert           | forest       | roc-auc  |    0.491 |
| CYP3A4_Substrate_CarbonMangels | grover_large      | forest       | roc-auc  |    0.453 |

### CYP3A4_Veith (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| CYP3A4_Veith | **SOTA**          | -            | pr-auc   |    0.916 |
| CYP3A4_Veith | mat_masking_200k  | ridge        | pr-auc   |    0.836 |
| CYP3A4_Veith | rmat_4M_rdkit     | forest       | pr-auc   |    0.83  |
| CYP3A4_Veith | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.829 |
| CYP3A4_Veith | mat_masking_20M   | forest       | pr-auc   |    0.826 |
| CYP3A4_Veith | rmat_4M           | forest       | pr-auc   |    0.823 |
| CYP3A4_Veith | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.821 |
| CYP3A4_Veith | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.821 |
| CYP3A4_Veith | mat_masking_2M    | ridge        | pr-auc   |    0.82  |
| CYP3A4_Veith | mat_masking_2M    | forest       | pr-auc   |    0.819 |
| CYP3A4_Veith | mat_masking_20M   | ridge        | pr-auc   |    0.816 |
| CYP3A4_Veith | mat_masking_200k  | forest       | pr-auc   |    0.813 |
| CYP3A4_Veith | ChemBERTa-77M-MTR | ridge        | pr-auc   |    0.806 |
| CYP3A4_Veith | mol2vec           | forest       | pr-auc   |    0.801 |
| CYP3A4_Veith | ChemBERTa-10M-MTR | ridge        | pr-auc   |    0.798 |
| CYP3A4_Veith | ChemBERTa-5M-MTR  | ridge        | pr-auc   |    0.796 |
| CYP3A4_Veith | mol2vec           | ridge        | pr-auc   |    0.783 |
| CYP3A4_Veith | rmat_4M           | ridge        | pr-auc   |    0.76  |
| CYP3A4_Veith | rmat_4M_rdkit     | ridge        | pr-auc   |    0.756 |
| CYP3A4_Veith | grover_base       | ridge        | pr-auc   |    0.688 |
| CYP3A4_Veith | rmat_4M           | linear       | pr-auc   |    0.677 |
| CYP3A4_Veith | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.671 |
| CYP3A4_Veith | grover_large      | ridge        | pr-auc   |    0.671 |
| CYP3A4_Veith | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.67  |
| CYP3A4_Veith | rmat_4M_rdkit     | linear       | pr-auc   |    0.665 |
| CYP3A4_Veith | mat_masking_2M    | linear       | pr-auc   |    0.663 |
| CYP3A4_Veith | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.662 |
| CYP3A4_Veith | mat_masking_200k  | linear       | pr-auc   |    0.658 |
| CYP3A4_Veith | mat_masking_20M   | linear       | pr-auc   |    0.651 |
| CYP3A4_Veith | mol2vec           | linear       | pr-auc   |    0.645 |
| CYP3A4_Veith | grover_large      | forest       | pr-auc   |    0.643 |
| CYP3A4_Veith | grover_base       | forest       | pr-auc   |    0.628 |
| CYP3A4_Veith | grover_large      | linear       | pr-auc   |    0.586 |
| CYP3A4_Veith | grover_base       | linear       | pr-auc   |    0.574 |

### Caco2_Wang (regression)

| dataset    | base_model        | head_model   | metric   |   result |
|:-----------|:------------------|:-------------|:---------|---------:|
| Caco2_Wang | **SOTA**          | -            | mae      |    0.276 |
| Caco2_Wang | ChemBERTa-77M-MTR | ridge        | mae      |    0.291 |
| Caco2_Wang | mol2vec           | forest       | mae      |    0.301 |
| Caco2_Wang | rmat_4M_rdkit     | forest       | mae      |    0.309 |
| Caco2_Wang | ChemBERTa-10M-MTR | forest       | mae      |    0.321 |
| Caco2_Wang | mat_masking_20M   | forest       | mae      |    0.325 |
| Caco2_Wang | ChemBERTa-10M-MTR | ridge        | mae      |    0.332 |
| Caco2_Wang | ChemBERTa-5M-MTR  | forest       | mae      |    0.333 |
| Caco2_Wang | rmat_4M           | forest       | mae      |    0.334 |
| Caco2_Wang | mat_masking_200k  | forest       | mae      |    0.336 |
| Caco2_Wang | ChemBERTa-77M-MTR | forest       | mae      |    0.337 |
| Caco2_Wang | mol2vec           | ridge        | mae      |    0.338 |
| Caco2_Wang | mat_masking_200k  | ridge        | mae      |    0.342 |
| Caco2_Wang | ChemBERTa-5M-MTR  | ridge        | mae      |    0.348 |
| Caco2_Wang | mat_masking_2M    | forest       | mae      |    0.367 |
| Caco2_Wang | ChemBERTa-77M-MTR | linear       | mae      |    0.437 |
| Caco2_Wang | ChemBERTa-10M-MTR | linear       | mae      |    0.45  |
| Caco2_Wang | rmat_4M           | ridge        | mae      |    0.451 |
| Caco2_Wang | mat_masking_2M    | ridge        | mae      |    0.475 |
| Caco2_Wang | grover_large      | forest       | mae      |    0.48  |
| Caco2_Wang | grover_base       | forest       | mae      |    0.488 |
| Caco2_Wang | rmat_4M_rdkit     | ridge        | mae      |    0.493 |
| Caco2_Wang | mat_masking_20M   | ridge        | mae      |    0.497 |
| Caco2_Wang | grover_base       | ridge        | mae      |    0.5   |
| Caco2_Wang | grover_large      | ridge        | mae      |    0.523 |
| Caco2_Wang | molbert           | ridge        | mae      |    0.591 |
| Caco2_Wang | molbert           | forest       | mae      |    0.599 |
| Caco2_Wang | mol2vec           | linear       | mae      |    0.611 |
| Caco2_Wang | rmat_4M_rdkit     | linear       | mae      |    0.727 |
| Caco2_Wang | grover_large      | linear       | mae      |    0.741 |
| Caco2_Wang | grover_base       | linear       | mae      |    0.788 |
| Caco2_Wang | rmat_4M           | linear       | mae      |    0.809 |
| Caco2_Wang | ChemBERTa-5M-MTR  | linear       | mae      |    0.914 |
| Caco2_Wang | mat_masking_200k  | linear       | mae      |    5.092 |
| Caco2_Wang | mat_masking_20M   | linear       | mae      |    6.734 |
| Caco2_Wang | mat_masking_2M    | linear       | mae      |   17.69  |

### Clearance_Hepatocyte_AZ (regression)

| dataset                 | base_model        | head_model   | metric   |   result |
|:------------------------|:------------------|:-------------|:---------|---------:|
| Clearance_Hepatocyte_AZ | **SOTA**          | -            | spearman |    0.536 |
| Clearance_Hepatocyte_AZ | ChemBERTa-77M-MTR | forest       | spearman |    0.375 |
| Clearance_Hepatocyte_AZ | ChemBERTa-10M-MTR | forest       | spearman |    0.361 |
| Clearance_Hepatocyte_AZ | mol2vec           | forest       | spearman |    0.356 |
| Clearance_Hepatocyte_AZ | mol2vec           | linear       | spearman |    0.298 |
| Clearance_Hepatocyte_AZ | mat_masking_200k  | forest       | spearman |    0.298 |
| Clearance_Hepatocyte_AZ | mol2vec           | ridge        | spearman |    0.298 |
| Clearance_Hepatocyte_AZ | ChemBERTa-5M-MTR  | forest       | spearman |    0.291 |
| Clearance_Hepatocyte_AZ | grover_base       | linear       | spearman |    0.286 |
| Clearance_Hepatocyte_AZ | mat_masking_2M    | forest       | spearman |    0.278 |
| Clearance_Hepatocyte_AZ | mat_masking_20M   | forest       | spearman |    0.27  |
| Clearance_Hepatocyte_AZ | grover_base       | ridge        | spearman |    0.257 |
| Clearance_Hepatocyte_AZ | rmat_4M_rdkit     | ridge        | spearman |    0.244 |
| Clearance_Hepatocyte_AZ | ChemBERTa-77M-MTR | linear       | spearman |    0.224 |
| Clearance_Hepatocyte_AZ | ChemBERTa-77M-MTR | ridge        | spearman |    0.221 |
| Clearance_Hepatocyte_AZ | ChemBERTa-10M-MTR | ridge        | spearman |    0.213 |
| Clearance_Hepatocyte_AZ | ChemBERTa-10M-MTR | linear       | spearman |    0.213 |
| Clearance_Hepatocyte_AZ | mat_masking_200k  | linear       | spearman |    0.205 |
| Clearance_Hepatocyte_AZ | mat_masking_2M    | ridge        | spearman |    0.202 |
| Clearance_Hepatocyte_AZ | ChemBERTa-5M-MTR  | ridge        | spearman |    0.186 |
| Clearance_Hepatocyte_AZ | ChemBERTa-5M-MTR  | linear       | spearman |    0.185 |
| Clearance_Hepatocyte_AZ | rmat_4M           | ridge        | spearman |    0.162 |
| Clearance_Hepatocyte_AZ | mat_masking_2M    | linear       | spearman |    0.143 |
| Clearance_Hepatocyte_AZ | mat_masking_200k  | ridge        | spearman |    0.136 |
| Clearance_Hepatocyte_AZ | grover_large      | ridge        | spearman |    0.128 |
| Clearance_Hepatocyte_AZ | mat_masking_20M   | ridge        | spearman |    0.126 |
| Clearance_Hepatocyte_AZ | grover_base       | forest       | spearman |    0.084 |
| Clearance_Hepatocyte_AZ | grover_large      | linear       | spearman |    0.083 |
| Clearance_Hepatocyte_AZ | rmat_4M           | linear       | spearman |    0.073 |
| Clearance_Hepatocyte_AZ | mat_masking_20M   | linear       | spearman |    0.044 |
| Clearance_Hepatocyte_AZ | molbert           | forest       | spearman |   -0.008 |
| Clearance_Hepatocyte_AZ | molbert           | ridge        | spearman |   -0.02  |
| Clearance_Hepatocyte_AZ | rmat_4M_rdkit     | linear       | spearman |   -0.059 |

### HIA_Hou (classification)

| dataset   | base_model        | head_model   | metric   |   result |
|:----------|:------------------|:-------------|:---------|---------:|
| HIA_Hou   | **SOTA**          | -            | roc-auc  |    0.989 |
| HIA_Hou   | mat_masking_200k  | forest       | roc-auc  |    0.984 |
| HIA_Hou   | mol2vec           | forest       | roc-auc  |    0.978 |
| HIA_Hou   | mat_masking_2M    | forest       | roc-auc  |    0.976 |
| HIA_Hou   | rmat_4M_rdkit     | forest       | roc-auc  |    0.974 |
| HIA_Hou   | mat_masking_20M   | forest       | roc-auc  |    0.971 |
| HIA_Hou   | rmat_4M           | forest       | roc-auc  |    0.97  |
| HIA_Hou   | mat_masking_2M    | ridge        | roc-auc  |    0.96  |
| HIA_Hou   | rmat_4M_rdkit     | ridge        | roc-auc  |    0.96  |
| HIA_Hou   | mat_masking_20M   | ridge        | roc-auc  |    0.957 |
| HIA_Hou   | mat_masking_200k  | ridge        | roc-auc  |    0.957 |
| HIA_Hou   | rmat_4M           | ridge        | roc-auc  |    0.956 |
| HIA_Hou   | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.952 |
| HIA_Hou   | ChemBERTa-77M-MTR | ridge        | roc-auc  |    0.949 |
| HIA_Hou   | rmat_4M_rdkit     | linear       | roc-auc  |    0.933 |
| HIA_Hou   | rmat_4M           | linear       | roc-auc  |    0.933 |
| HIA_Hou   | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.929 |
| HIA_Hou   | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.928 |
| HIA_Hou   | mol2vec           | linear       | roc-auc  |    0.917 |
| HIA_Hou   | mat_masking_20M   | linear       | roc-auc  |    0.902 |
| HIA_Hou   | mat_masking_2M    | linear       | roc-auc  |    0.891 |
| HIA_Hou   | mat_masking_200k  | linear       | roc-auc  |    0.867 |
| HIA_Hou   | mol2vec           | ridge        | roc-auc  |    0.86  |
| HIA_Hou   | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.859 |
| HIA_Hou   | ChemBERTa-10M-MTR | ridge        | roc-auc  |    0.858 |
| HIA_Hou   | grover_base       | forest       | roc-auc  |    0.855 |
| HIA_Hou   | ChemBERTa-5M-MTR  | ridge        | roc-auc  |    0.854 |
| HIA_Hou   | grover_large      | forest       | roc-auc  |    0.848 |
| HIA_Hou   | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.843 |
| HIA_Hou   | grover_large      | ridge        | roc-auc  |    0.841 |
| HIA_Hou   | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.817 |
| HIA_Hou   | grover_base       | ridge        | roc-auc  |    0.781 |
| HIA_Hou   | grover_large      | linear       | roc-auc  |    0.676 |
| HIA_Hou   | grover_base       | linear       | roc-auc  |    0.672 |
| HIA_Hou   | molbert           | forest       | roc-auc  |    0.569 |

### Half_Life_Obach (regression)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| Half_Life_Obach | **SOTA**          | -            | spearman |    0.576 |
| Half_Life_Obach | mol2vec           | forest       | spearman |    0.425 |
| Half_Life_Obach | mat_masking_200k  | forest       | spearman |    0.364 |
| Half_Life_Obach | mat_masking_2M    | forest       | spearman |    0.361 |
| Half_Life_Obach | rmat_4M_rdkit     | forest       | spearman |    0.354 |
| Half_Life_Obach | rmat_4M           | forest       | spearman |    0.305 |
| Half_Life_Obach | mat_masking_20M   | forest       | spearman |    0.29  |
| Half_Life_Obach | ChemBERTa-10M-MTR | forest       | spearman |    0.267 |
| Half_Life_Obach | ChemBERTa-77M-MTR | forest       | spearman |    0.218 |
| Half_Life_Obach | ChemBERTa-5M-MTR  | forest       | spearman |    0.182 |
| Half_Life_Obach | mat_masking_200k  | linear       | spearman |    0.144 |
| Half_Life_Obach | grover_large      | forest       | spearman |    0.132 |
| Half_Life_Obach | ChemBERTa-5M-MTR  | ridge        | spearman |    0.131 |
| Half_Life_Obach | ChemBERTa-5M-MTR  | linear       | spearman |    0.115 |
| Half_Life_Obach | rmat_4M_rdkit     | linear       | spearman |    0.11  |
| Half_Life_Obach | rmat_4M_rdkit     | ridge        | spearman |    0.097 |
| Half_Life_Obach | grover_base       | ridge        | spearman |    0.096 |
| Half_Life_Obach | mat_masking_20M   | linear       | spearman |    0.092 |
| Half_Life_Obach | mat_masking_20M   | ridge        | spearman |    0.089 |
| Half_Life_Obach | mat_masking_200k  | ridge        | spearman |    0.087 |
| Half_Life_Obach | mat_masking_2M    | ridge        | spearman |    0.085 |
| Half_Life_Obach | grover_base       | linear       | spearman |    0.081 |
| Half_Life_Obach | mat_masking_2M    | linear       | spearman |    0.078 |
| Half_Life_Obach | grover_base       | forest       | spearman |    0.05  |
| Half_Life_Obach | mol2vec           | ridge        | spearman |    0.049 |
| Half_Life_Obach | mol2vec           | linear       | spearman |    0.047 |
| Half_Life_Obach | grover_large      | linear       | spearman |    0.044 |
| Half_Life_Obach | rmat_4M           | linear       | spearman |    0.037 |
| Half_Life_Obach | rmat_4M           | ridge        | spearman |    0.034 |
| Half_Life_Obach | grover_large      | ridge        | spearman |    0.026 |
| Half_Life_Obach | molbert           | ridge        | spearman |    0.023 |
| Half_Life_Obach | molbert           | forest       | spearman |    0.023 |
| Half_Life_Obach | ChemBERTa-77M-MTR | linear       | spearman |    0.019 |
| Half_Life_Obach | ChemBERTa-77M-MTR | ridge        | spearman |    0.008 |
| Half_Life_Obach | ChemBERTa-10M-MTR | linear       | spearman |   -0.021 |
| Half_Life_Obach | ChemBERTa-10M-MTR | ridge        | spearman |   -0.036 |

### Lipophilicity_AstraZeneca (regression)

| dataset                   | base_model        | head_model   | metric   |   result |
|:--------------------------|:------------------|:-------------|:---------|---------:|
| Lipophilicity_AstraZeneca | **SOTA**          | -            | mae      |    0.467 |
| Lipophilicity_AstraZeneca | rmat_4M           | ridge        | mae      |    0.527 |
| Lipophilicity_AstraZeneca | mat_masking_2M    | ridge        | mae      |    0.536 |
| Lipophilicity_AstraZeneca | rmat_4M_rdkit     | ridge        | mae      |    0.537 |
| Lipophilicity_AstraZeneca | mat_masking_20M   | ridge        | mae      |    0.554 |
| Lipophilicity_AstraZeneca | mat_masking_200k  | ridge        | mae      |    0.568 |
| Lipophilicity_AstraZeneca | ChemBERTa-77M-MTR | ridge        | mae      |    0.59  |
| Lipophilicity_AstraZeneca | ChemBERTa-10M-MTR | ridge        | mae      |    0.596 |
| Lipophilicity_AstraZeneca | ChemBERTa-77M-MTR | linear       | mae      |    0.598 |
| Lipophilicity_AstraZeneca | ChemBERTa-10M-MTR | linear       | mae      |    0.603 |
| Lipophilicity_AstraZeneca | mat_masking_2M    | linear       | mae      |    0.604 |
| Lipophilicity_AstraZeneca | mat_masking_200k  | linear       | mae      |    0.609 |
| Lipophilicity_AstraZeneca | ChemBERTa-5M-MTR  | ridge        | mae      |    0.61  |
| Lipophilicity_AstraZeneca | mat_masking_20M   | linear       | mae      |    0.61  |
| Lipophilicity_AstraZeneca | ChemBERTa-5M-MTR  | linear       | mae      |    0.619 |
| Lipophilicity_AstraZeneca | mol2vec           | ridge        | mae      |    0.654 |
| Lipophilicity_AstraZeneca | mol2vec           | linear       | mae      |    0.659 |
| Lipophilicity_AstraZeneca | ChemBERTa-10M-MTR | forest       | mae      |    0.686 |
| Lipophilicity_AstraZeneca | ChemBERTa-5M-MTR  | forest       | mae      |    0.728 |
| Lipophilicity_AstraZeneca | ChemBERTa-77M-MTR | forest       | mae      |    0.728 |
| Lipophilicity_AstraZeneca | mol2vec           | forest       | mae      |    0.804 |
| Lipophilicity_AstraZeneca | grover_large      | ridge        | mae      |    0.834 |
| Lipophilicity_AstraZeneca | grover_base       | ridge        | mae      |    0.849 |
| Lipophilicity_AstraZeneca | molbert           | forest       | mae      |    0.983 |
| Lipophilicity_AstraZeneca | molbert           | ridge        | mae      |    0.987 |
| Lipophilicity_AstraZeneca | grover_base       | linear       | mae      |    1.019 |
| Lipophilicity_AstraZeneca | grover_large      | linear       | mae      |    1.333 |
| Lipophilicity_AstraZeneca | rmat_4M           | linear       | mae      |    1.668 |
| Lipophilicity_AstraZeneca | rmat_4M_rdkit     | linear       | mae      |    2.935 |

### Pgp_Broccatelli (classification)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| Pgp_Broccatelli | **SOTA**          | -            | roc-auc  |    0.938 |
| Pgp_Broccatelli | rmat_4M           | forest       | roc-auc  |    0.923 |
| Pgp_Broccatelli | rmat_4M_rdkit     | forest       | roc-auc  |    0.916 |
| Pgp_Broccatelli | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.915 |
| Pgp_Broccatelli | mat_masking_20M   | forest       | roc-auc  |    0.911 |
| Pgp_Broccatelli | mat_masking_2M    | forest       | roc-auc  |    0.91  |
| Pgp_Broccatelli | mat_masking_200k  | forest       | roc-auc  |    0.906 |
| Pgp_Broccatelli | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.903 |
| Pgp_Broccatelli | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.891 |
| Pgp_Broccatelli | mol2vec           | forest       | roc-auc  |    0.887 |
| Pgp_Broccatelli | mol2vec           | ridge        | roc-auc  |    0.877 |
| Pgp_Broccatelli | mat_masking_2M    | linear       | roc-auc  |    0.849 |
| Pgp_Broccatelli | mat_masking_200k  | linear       | roc-auc  |    0.849 |
| Pgp_Broccatelli | ChemBERTa-5M-MTR  | ridge        | roc-auc  |    0.839 |
| Pgp_Broccatelli | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.833 |
| Pgp_Broccatelli | ChemBERTa-77M-MTR | ridge        | roc-auc  |    0.825 |
| Pgp_Broccatelli | grover_base       | forest       | roc-auc  |    0.824 |
| Pgp_Broccatelli | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.813 |
| Pgp_Broccatelli | grover_large      | forest       | roc-auc  |    0.812 |
| Pgp_Broccatelli | mat_masking_20M   | linear       | roc-auc  |    0.808 |
| Pgp_Broccatelli | ChemBERTa-10M-MTR | ridge        | roc-auc  |    0.806 |
| Pgp_Broccatelli | mol2vec           | linear       | roc-auc  |    0.804 |
| Pgp_Broccatelli | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.792 |
| Pgp_Broccatelli | grover_large      | ridge        | roc-auc  |    0.778 |
| Pgp_Broccatelli | rmat_4M_rdkit     | ridge        | roc-auc  |    0.776 |
| Pgp_Broccatelli | rmat_4M           | ridge        | roc-auc  |    0.763 |
| Pgp_Broccatelli | grover_base       | ridge        | roc-auc  |    0.752 |
| Pgp_Broccatelli | mat_masking_20M   | ridge        | roc-auc  |    0.752 |
| Pgp_Broccatelli | rmat_4M           | linear       | roc-auc  |    0.751 |
| Pgp_Broccatelli | rmat_4M_rdkit     | linear       | roc-auc  |    0.747 |
| Pgp_Broccatelli | grover_base       | linear       | roc-auc  |    0.738 |
| Pgp_Broccatelli | mat_masking_200k  | ridge        | roc-auc  |    0.712 |
| Pgp_Broccatelli | grover_large      | linear       | roc-auc  |    0.702 |
| Pgp_Broccatelli | mat_masking_2M    | ridge        | roc-auc  |    0.615 |
| Pgp_Broccatelli | molbert           | forest       | roc-auc  |    0.525 |

### Solubility_AqSolDB (regression)

| dataset            | base_model        | head_model   | metric   |   result |
|:-------------------|:------------------|:-------------|:---------|---------:|
| Solubility_AqSolDB | **SOTA**          | -            | mae      |    0.761 |
| Solubility_AqSolDB | rmat_4M_rdkit     | ridge        | mae      |    0.807 |
| Solubility_AqSolDB | mat_masking_20M   | ridge        | mae      |    0.823 |
| Solubility_AqSolDB | mat_masking_200k  | ridge        | mae      |    0.835 |
| Solubility_AqSolDB | rmat_4M           | ridge        | mae      |    0.84  |
| Solubility_AqSolDB | mat_masking_2M    | ridge        | mae      |    0.856 |
| Solubility_AqSolDB | mat_masking_20M   | linear       | mae      |    0.871 |
| Solubility_AqSolDB | mat_masking_200k  | linear       | mae      |    0.885 |
| Solubility_AqSolDB | mat_masking_2M    | linear       | mae      |    0.904 |
| Solubility_AqSolDB | ChemBERTa-10M-MTR | ridge        | mae      |    0.938 |
| Solubility_AqSolDB | ChemBERTa-77M-MTR | ridge        | mae      |    0.944 |
| Solubility_AqSolDB | ChemBERTa-10M-MTR | linear       | mae      |    0.951 |
| Solubility_AqSolDB | ChemBERTa-77M-MTR | linear       | mae      |    0.965 |
| Solubility_AqSolDB | ChemBERTa-5M-MTR  | ridge        | mae      |    0.991 |
| Solubility_AqSolDB | mol2vec           | forest       | mae      |    1.014 |
| Solubility_AqSolDB | ChemBERTa-5M-MTR  | linear       | mae      |    1.021 |
| Solubility_AqSolDB | rmat_4M           | linear       | mae      |    1.119 |
| Solubility_AqSolDB | rmat_4M_rdkit     | linear       | mae      |    1.134 |
| Solubility_AqSolDB | mol2vec           | ridge        | mae      |    1.151 |
| Solubility_AqSolDB | mol2vec           | linear       | mae      |    1.164 |
| Solubility_AqSolDB | grover_large      | ridge        | mae      |    1.197 |
| Solubility_AqSolDB | grover_base       | ridge        | mae      |    1.203 |
| Solubility_AqSolDB | grover_base       | linear       | mae      |    1.252 |
| Solubility_AqSolDB | grover_large      | linear       | mae      |    1.342 |

### VDss_Lombardo (regression)

| dataset       | base_model        | head_model   | metric   |   result |
|:--------------|:------------------|:-------------|:---------|---------:|
| VDss_Lombardo | **SOTA**          | -            | spearman |    0.713 |
| VDss_Lombardo | mat_masking_2M    | forest       | spearman |    0.446 |
| VDss_Lombardo | mat_masking_20M   | forest       | spearman |    0.426 |
| VDss_Lombardo | ChemBERTa-77M-MTR | forest       | spearman |    0.401 |
| VDss_Lombardo | mol2vec           | forest       | spearman |    0.382 |
| VDss_Lombardo | ChemBERTa-10M-MTR | forest       | spearman |    0.371 |
| VDss_Lombardo | mat_masking_200k  | forest       | spearman |    0.345 |
| VDss_Lombardo | ChemBERTa-10M-MTR | linear       | spearman |    0.284 |
| VDss_Lombardo | ChemBERTa-10M-MTR | ridge        | spearman |    0.284 |
| VDss_Lombardo | ChemBERTa-5M-MTR  | forest       | spearman |    0.278 |
| VDss_Lombardo | ChemBERTa-77M-MTR | ridge        | spearman |    0.153 |
| VDss_Lombardo | ChemBERTa-77M-MTR | linear       | spearman |    0.149 |
| VDss_Lombardo | mat_masking_20M   | ridge        | spearman |    0.147 |
| VDss_Lombardo | mol2vec           | ridge        | spearman |    0.136 |
| VDss_Lombardo | mol2vec           | linear       | spearman |    0.136 |
| VDss_Lombardo | mat_masking_200k  | ridge        | spearman |    0.104 |
| VDss_Lombardo | mat_masking_20M   | linear       | spearman |    0.07  |
| VDss_Lombardo | grover_base       | linear       | spearman |    0.054 |
| VDss_Lombardo | grover_base       | ridge        | spearman |    0.054 |
| VDss_Lombardo | rmat_4M           | linear       | spearman |    0.048 |
| VDss_Lombardo | rmat_4M           | ridge        | spearman |    0.044 |
| VDss_Lombardo | grover_large      | ridge        | spearman |    0.044 |
| VDss_Lombardo | mat_masking_200k  | linear       | spearman |    0.044 |
| VDss_Lombardo | rmat_4M_rdkit     | linear       | spearman |    0.043 |
| VDss_Lombardo | mat_masking_2M    | linear       | spearman |    0.04  |
| VDss_Lombardo | mat_masking_2M    | ridge        | spearman |    0.038 |
| VDss_Lombardo | grover_large      | linear       | spearman |    0.03  |
| VDss_Lombardo | molbert           | forest       | spearman |    0.027 |
| VDss_Lombardo | molbert           | ridge        | spearman |    0.024 |
| VDss_Lombardo | rmat_4M_rdkit     | ridge        | spearman |    0.018 |
| VDss_Lombardo | ChemBERTa-5M-MTR  | linear       | spearman |   -0.014 |
| VDss_Lombardo | ChemBERTa-5M-MTR  | ridge        | spearman |   -0.015 |

### ogbg-molbace (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| ogbg-molbace | rmat_4M_rdkit     | forest       | rocauc   | 0.83116  |
| ogbg-molbace | ChemBERTa-10M-MTR | forest       | rocauc   | 0.822987 |
| ogbg-molbace | mat_masking_2M    | forest       | rocauc   | 0.822292 |
| ogbg-molbace | rmat_4M           | forest       | rocauc   | 0.81977  |
| ogbg-molbace | ChemBERTa-77M-MTR | forest       | rocauc   | 0.81012  |
| ogbg-molbace | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.804903 |
| ogbg-molbace | mat_masking_200k  | forest       | rocauc   | 0.79847  |
| ogbg-molbace | mat_masking_20M   | forest       | rocauc   | 0.797774 |
| ogbg-molbace | mol2vec           | forest       | rocauc   | 0.797079 |
| ogbg-molbace | mol2vec           | ridge        | rocauc   | 0.740741 |
| ogbg-molbace | ChemBERTa-5M-MTR  | ridge        | rocauc   | 0.736394 |
| ogbg-molbace | grover_base       | forest       | rocauc   | 0.715528 |
| ogbg-molbace | mat_masking_20M   | linear       | rocauc   | 0.683533 |
| ogbg-molbace | ChemBERTa-10M-MTR | ridge        | rocauc   | 0.675535 |
| ogbg-molbace | ChemBERTa-77M-MTR | ridge        | rocauc   | 0.673274 |
| ogbg-molbace | grover_large      | forest       | rocauc   | 0.672057 |
| ogbg-molbace | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.66771  |
| ogbg-molbace | rmat_4M           | linear       | rocauc   | 0.665971 |
| ogbg-molbace | ChemBERTa-10M-MTR | linear       | rocauc   | 0.664145 |
| ogbg-molbace | mat_masking_2M    | linear       | rocauc   | 0.663276 |
| ogbg-molbace | ChemBERTa-77M-MTR | linear       | rocauc   | 0.662407 |
| ogbg-molbace | mat_masking_200k  | linear       | rocauc   | 0.645627 |
| ogbg-molbace | mat_masking_200k  | ridge        | rocauc   | 0.640758 |
| ogbg-molbace | mat_masking_2M    | ridge        | rocauc   | 0.64041  |
| ogbg-molbace | molbert           | forest       | rocauc   | 0.631542 |
| ogbg-molbace | rmat_4M_rdkit     | linear       | rocauc   | 0.61485  |
| ogbg-molbace | mol2vec           | linear       | rocauc   | 0.609546 |
| ogbg-molbace | rmat_4M_rdkit     | ridge        | rocauc   | 0.600591 |
| ogbg-molbace | rmat_4M           | ridge        | rocauc   | 0.591723 |
| ogbg-molbace | grover_base       | linear       | rocauc   | 0.587463 |
| ogbg-molbace | grover_base       | ridge        | rocauc   | 0.580247 |
| ogbg-molbace | grover_large      | linear       | rocauc   | 0.546166 |
| ogbg-molbace | mat_masking_20M   | ridge        | rocauc   | 0.543905 |
| ogbg-molbace | grover_large      | ridge        | rocauc   | 0.473657 |

### ogbg-molbbbp (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| ogbg-molbbbp | ChemBERTa-77M-MTR | ridge        | rocauc   | 0.754871 |
| ogbg-molbbbp | mol2vec           | forest       | rocauc   | 0.733893 |
| ogbg-molbbbp | ChemBERTa-10M-MTR | ridge        | rocauc   | 0.733748 |
| ogbg-molbbbp | rmat_4M_rdkit     | forest       | rocauc   | 0.723958 |
| ogbg-molbbbp | ChemBERTa-5M-MTR  | ridge        | rocauc   | 0.717159 |
| ogbg-molbbbp | rmat_4M           | forest       | rocauc   | 0.713638 |
| ogbg-molbbbp | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.707224 |
| ogbg-molbbbp | mat_masking_20M   | forest       | rocauc   | 0.706694 |
| ogbg-molbbbp | ChemBERTa-10M-MTR | forest       | rocauc   | 0.704041 |
| ogbg-molbbbp | mat_masking_200k  | forest       | rocauc   | 0.700231 |
| ogbg-molbbbp | ChemBERTa-77M-MTR | forest       | rocauc   | 0.695264 |
| ogbg-molbbbp | mat_masking_2M    | forest       | rocauc   | 0.694348 |
| ogbg-molbbbp | mol2vec           | ridge        | rocauc   | 0.671682 |
| ogbg-molbbbp | mat_masking_20M   | ridge        | rocauc   | 0.669657 |
| ogbg-molbbbp | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.668981 |
| ogbg-molbbbp | ChemBERTa-77M-MTR | linear       | rocauc   | 0.659144 |
| ogbg-molbbbp | rmat_4M_rdkit     | linear       | rocauc   | 0.656829 |
| ogbg-molbbbp | mat_masking_2M    | ridge        | rocauc   | 0.652392 |
| ogbg-molbbbp | ChemBERTa-10M-MTR | linear       | rocauc   | 0.633681 |
| ogbg-molbbbp | rmat_4M           | ridge        | rocauc   | 0.633102 |
| ogbg-molbbbp | rmat_4M           | linear       | rocauc   | 0.632523 |
| ogbg-molbbbp | mat_masking_200k  | ridge        | rocauc   | 0.630498 |
| ogbg-molbbbp | mat_masking_2M    | linear       | rocauc   | 0.59838  |
| ogbg-molbbbp | mol2vec           | linear       | rocauc   | 0.594329 |
| ogbg-molbbbp | grover_large      | linear       | rocauc   | 0.583333 |
| ogbg-molbbbp | mat_masking_200k  | linear       | rocauc   | 0.578125 |
| ogbg-molbbbp | grover_base       | linear       | rocauc   | 0.576389 |
| ogbg-molbbbp | grover_base       | forest       | rocauc   | 0.569782 |
| ogbg-molbbbp | mat_masking_20M   | linear       | rocauc   | 0.566551 |
| ogbg-molbbbp | grover_large      | forest       | rocauc   | 0.563947 |
| ogbg-molbbbp | grover_large      | ridge        | rocauc   | 0.542438 |
| ogbg-molbbbp | molbert           | forest       | rocauc   | 0.530527 |
| ogbg-molbbbp | grover_base       | ridge        | rocauc   | 0.525752 |
| ogbg-molbbbp | rmat_4M_rdkit     | ridge        | rocauc   | 0.522859 |

### ogbg-molclintox (classification)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| ogbg-molclintox | ChemBERTa-5M-MTR  | ridge        | rocauc   | 0.981062 |
| ogbg-molclintox | ChemBERTa-10M-MTR | forest       | rocauc   | 0.954842 |
| ogbg-molclintox | ChemBERTa-10M-MTR | ridge        | rocauc   | 0.949383 |
| ogbg-molclintox | ChemBERTa-77M-MTR | forest       | rocauc   | 0.946376 |
| ogbg-molclintox | molbert           | forest       | rocauc   | 0.925998 |
| ogbg-molclintox | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.921768 |
| ogbg-molclintox | ChemBERTa-10M-MTR | linear       | rocauc   | 0.892646 |
| ogbg-molclintox | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.890834 |
| ogbg-molclintox | mol2vec           | ridge        | rocauc   | 0.870281 |
| ogbg-molclintox | ChemBERTa-77M-MTR | ridge        | rocauc   | 0.852972 |
| ogbg-molclintox | mat_masking_20M   | forest       | rocauc   | 0.852807 |
| ogbg-molclintox | rmat_4M_rdkit     | forest       | rocauc   | 0.849005 |
| ogbg-molclintox | mat_masking_2M    | forest       | rocauc   | 0.845249 |
| ogbg-molclintox | ChemBERTa-77M-MTR | linear       | rocauc   | 0.838057 |
| ogbg-molclintox | mat_masking_200k  | forest       | rocauc   | 0.821976 |
| ogbg-molclintox | mol2vec           | linear       | rocauc   | 0.791085 |
| ogbg-molclintox | rmat_4M_rdkit     | linear       | rocauc   | 0.755689 |
| ogbg-molclintox | rmat_4M           | linear       | rocauc   | 0.752079 |
| ogbg-molclintox | mat_masking_2M    | linear       | rocauc   | 0.747637 |
| ogbg-molclintox | rmat_4M           | forest       | rocauc   | 0.73537  |
| ogbg-molclintox | mat_masking_20M   | linear       | rocauc   | 0.700281 |
| ogbg-molclintox | mat_masking_200k  | linear       | rocauc   | 0.69306  |
| ogbg-molclintox | mat_masking_200k  | ridge        | rocauc   | 0.658782 |
| ogbg-molclintox | mat_masking_20M   | ridge        | rocauc   | 0.652369 |
| ogbg-molclintox | grover_large      | ridge        | rocauc   | 0.639896 |
| ogbg-molclintox | rmat_4M_rdkit     | ridge        | rocauc   | 0.619408 |
| ogbg-molclintox | mol2vec           | forest       | rocauc   | 0.616624 |
| ogbg-molclintox | grover_base       | forest       | rocauc   | 0.61304  |
| ogbg-molclintox | rmat_4M           | ridge        | rocauc   | 0.601295 |
| ogbg-molclintox | mat_masking_2M    | ridge        | rocauc   | 0.597437 |
| ogbg-molclintox | grover_large      | linear       | rocauc   | 0.587247 |
| ogbg-molclintox | grover_base       | linear       | rocauc   | 0.564045 |
| ogbg-molclintox | grover_large      | forest       | rocauc   | 0.546847 |
| ogbg-molclintox | grover_base       | ridge        | rocauc   | 0.534659 |

### ogbg-molesol (regression)

| dataset      | base_model        | head_model   | metric   |     result |
|:-------------|:------------------|:-------------|:---------|-----------:|
| ogbg-molesol | rmat_4M_rdkit     | forest       | rmse     |   0.79471  |
| ogbg-molesol | mat_masking_2M    | ridge        | rmse     |   0.837066 |
| ogbg-molesol | mat_masking_200k  | ridge        | rmse     |   0.862999 |
| ogbg-molesol | mat_masking_20M   | forest       | rmse     |   0.896521 |
| ogbg-molesol | ChemBERTa-77M-MTR | ridge        | rmse     |   0.900927 |
| ogbg-molesol | ChemBERTa-5M-MTR  | ridge        | rmse     |   0.905719 |
| ogbg-molesol | ChemBERTa-10M-MTR | forest       | rmse     |   0.916418 |
| ogbg-molesol | rmat_4M_rdkit     | ridge        | rmse     |   0.929571 |
| ogbg-molesol | ChemBERTa-10M-MTR | ridge        | rmse     |   0.930629 |
| ogbg-molesol | mat_masking_20M   | ridge        | rmse     |   0.933371 |
| ogbg-molesol | rmat_4M           | ridge        | rmse     |   0.945444 |
| ogbg-molesol | mat_masking_2M    | forest       | rmse     |   0.951971 |
| ogbg-molesol | ChemBERTa-77M-MTR | forest       | rmse     |   0.988451 |
| ogbg-molesol | ChemBERTa-5M-MTR  | forest       | rmse     |   0.999667 |
| ogbg-molesol | rmat_4M           | forest       | rmse     |   1.05733  |
| ogbg-molesol | mol2vec           | forest       | rmse     |   1.06629  |
| ogbg-molesol | mat_masking_200k  | forest       | rmse     |   1.07043  |
| ogbg-molesol | mol2vec           | ridge        | rmse     |   1.13732  |
| ogbg-molesol | ChemBERTa-10M-MTR | linear       | rmse     |   1.35933  |
| ogbg-molesol | grover_base       | ridge        | rmse     |   1.42118  |
| ogbg-molesol | grover_large      | ridge        | rmse     |   1.55571  |
| ogbg-molesol | ChemBERTa-5M-MTR  | linear       | rmse     |   1.58274  |
| ogbg-molesol | mol2vec           | linear       | rmse     |   1.60867  |
| ogbg-molesol | grover_large      | forest       | rmse     |   1.62247  |
| ogbg-molesol | ChemBERTa-77M-MTR | linear       | rmse     |   1.63884  |
| ogbg-molesol | grover_base       | forest       | rmse     |   1.71492  |
| ogbg-molesol | molbert           | forest       | rmse     |   1.89208  |
| ogbg-molesol | molbert           | ridge        | rmse     |   2.1248   |
| ogbg-molesol | grover_large      | linear       | rmse     |   2.19911  |
| ogbg-molesol | grover_base       | linear       | rmse     |   2.31943  |
| ogbg-molesol | mat_masking_2M    | linear       | rmse     |  29.1458   |
| ogbg-molesol | mat_masking_20M   | linear       | rmse     |  52.8683   |
| ogbg-molesol | mat_masking_200k  | linear       | rmse     |  58.773    |
| ogbg-molesol | rmat_4M_rdkit     | linear       | rmse     | 172.599    |
| ogbg-molesol | rmat_4M           | linear       | rmse     | 300.781    |

### ogbg-molfreesolv (regression)

| dataset          | base_model        | head_model   | metric   |   result |
|:-----------------|:------------------|:-------------|:---------|---------:|
| ogbg-molfreesolv | rmat_4M_rdkit     | ridge        | rmse     |  2.03566 |
| ogbg-molfreesolv | rmat_4M           | ridge        | rmse     |  2.03691 |
| ogbg-molfreesolv | mat_masking_200k  | forest       | rmse     |  2.0406  |
| ogbg-molfreesolv | ChemBERTa-10M-MTR | ridge        | rmse     |  2.06668 |
| ogbg-molfreesolv | mat_masking_20M   | forest       | rmse     |  2.13132 |
| ogbg-molfreesolv | mat_masking_2M    | ridge        | rmse     |  2.24961 |
| ogbg-molfreesolv | ChemBERTa-5M-MTR  | ridge        | rmse     |  2.30062 |
| ogbg-molfreesolv | rmat_4M_rdkit     | forest       | rmse     |  2.30484 |
| ogbg-molfreesolv | ChemBERTa-5M-MTR  | forest       | rmse     |  2.32715 |
| ogbg-molfreesolv | ChemBERTa-10M-MTR | forest       | rmse     |  2.35527 |
| ogbg-molfreesolv | mat_masking_20M   | ridge        | rmse     |  2.37248 |
| ogbg-molfreesolv | rmat_4M           | linear       | rmse     |  2.45472 |
| ogbg-molfreesolv | mat_masking_200k  | ridge        | rmse     |  2.47561 |
| ogbg-molfreesolv | rmat_4M_rdkit     | linear       | rmse     |  2.47985 |
| ogbg-molfreesolv | rmat_4M           | forest       | rmse     |  2.53563 |
| ogbg-molfreesolv | ChemBERTa-77M-MTR | ridge        | rmse     |  2.67136 |
| ogbg-molfreesolv | grover_base       | ridge        | rmse     |  2.85304 |
| ogbg-molfreesolv | grover_large      | ridge        | rmse     |  3.00036 |
| ogbg-molfreesolv | ChemBERTa-77M-MTR | forest       | rmse     |  3.19246 |
| ogbg-molfreesolv | grover_base       | forest       | rmse     |  3.25353 |
| ogbg-molfreesolv | grover_large      | forest       | rmse     |  3.31627 |
| ogbg-molfreesolv | grover_large      | linear       | rmse     |  3.50614 |
| ogbg-molfreesolv | mol2vec           | forest       | rmse     |  3.63067 |
| ogbg-molfreesolv | grover_base       | linear       | rmse     |  3.9148  |
| ogbg-molfreesolv | molbert           | forest       | rmse     |  3.99995 |
| ogbg-molfreesolv | mol2vec           | ridge        | rmse     |  4.07396 |
| ogbg-molfreesolv | molbert           | ridge        | rmse     |  4.30471 |
| ogbg-molfreesolv | ChemBERTa-5M-MTR  | linear       | rmse     |  7.24826 |
| ogbg-molfreesolv | mat_masking_200k  | linear       | rmse     |  7.31636 |
| ogbg-molfreesolv | mat_masking_2M    | linear       | rmse     |  7.59417 |
| ogbg-molfreesolv | ChemBERTa-77M-MTR | linear       | rmse     |  7.63497 |
| ogbg-molfreesolv | ChemBERTa-10M-MTR | linear       | rmse     |  7.82469 |
| ogbg-molfreesolv | mat_masking_20M   | linear       | rmse     | 11.1612  |
| ogbg-molfreesolv | mol2vec           | linear       | rmse     | 38.6383  |

### ogbg-molhiv (classification)

| dataset     | base_model        | head_model   | metric   |   result |
|:------------|:------------------|:-------------|:---------|---------:|
| ogbg-molhiv | **SOTA**          | -            | rocauc   | 0.8475   |
| ogbg-molhiv | ChemBERTa-10M-MTR | forest       | rocauc   | 0.773587 |
| ogbg-molhiv | ChemBERTa-77M-MTR | forest       | rocauc   | 0.773509 |
| ogbg-molhiv | mol2vec           | forest       | rocauc   | 0.772772 |
| ogbg-molhiv | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.761573 |
| ogbg-molhiv | ChemBERTa-5M-MTR  | ridge        | rocauc   | 0.742703 |
| ogbg-molhiv | ChemBERTa-10M-MTR | ridge        | rocauc   | 0.738709 |
| ogbg-molhiv | ChemBERTa-77M-MTR | ridge        | rocauc   | 0.735047 |
| ogbg-molhiv | mol2vec           | ridge        | rocauc   | 0.716879 |
| ogbg-molhiv | grover_base       | ridge        | rocauc   | 0.701732 |
| ogbg-molhiv | grover_large      | ridge        | rocauc   | 0.62143  |
| ogbg-molhiv | mol2vec           | linear       | rocauc   | 0.574538 |
| ogbg-molhiv | ChemBERTa-77M-MTR | linear       | rocauc   | 0.571445 |
| ogbg-molhiv | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.567975 |
| ogbg-molhiv | ChemBERTa-10M-MTR | linear       | rocauc   | 0.556311 |
| ogbg-molhiv | grover_large      | linear       | rocauc   | 0.5357   |
| ogbg-molhiv | grover_base       | linear       | rocauc   | 0.518352 |

### ogbg-mollipo (regression)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| ogbg-mollipo | mat_masking_2M    | ridge        | rmse     | 0.732534 |
| ogbg-mollipo | rmat_4M           | ridge        | rmse     | 0.745979 |
| ogbg-mollipo | rmat_4M_rdkit     | ridge        | rmse     | 0.758755 |
| ogbg-mollipo | mat_masking_20M   | ridge        | rmse     | 0.762357 |
| ogbg-mollipo | mat_masking_200k  | ridge        | rmse     | 0.769099 |
| ogbg-mollipo | ChemBERTa-77M-MTR | ridge        | rmse     | 0.782462 |
| ogbg-mollipo | ChemBERTa-5M-MTR  | ridge        | rmse     | 0.785952 |
| ogbg-mollipo | ChemBERTa-5M-MTR  | linear       | rmse     | 0.795198 |
| ogbg-mollipo | ChemBERTa-77M-MTR | linear       | rmse     | 0.806851 |
| ogbg-mollipo | mat_masking_2M    | linear       | rmse     | 0.809546 |
| ogbg-mollipo | ChemBERTa-10M-MTR | ridge        | rmse     | 0.81547  |
| ogbg-mollipo | ChemBERTa-10M-MTR | forest       | rmse     | 0.831524 |
| ogbg-mollipo | ChemBERTa-5M-MTR  | forest       | rmse     | 0.838493 |
| ogbg-mollipo | ChemBERTa-10M-MTR | linear       | rmse     | 0.85315  |
| ogbg-mollipo | ChemBERTa-77M-MTR | forest       | rmse     | 0.863564 |
| ogbg-mollipo | mat_masking_200k  | linear       | rmse     | 0.870232 |
| ogbg-mollipo | mol2vec           | ridge        | rmse     | 0.875055 |
| ogbg-mollipo | mat_masking_20M   | linear       | rmse     | 0.875111 |
| ogbg-mollipo | mol2vec           | forest       | rmse     | 0.887032 |
| ogbg-mollipo | mol2vec           | linear       | rmse     | 0.896467 |
| ogbg-mollipo | grover_base       | ridge        | rmse     | 1.02419  |
| ogbg-mollipo | grover_large      | ridge        | rmse     | 1.03169  |
| ogbg-mollipo | molbert           | forest       | rmse     | 1.10014  |
| ogbg-mollipo | molbert           | ridge        | rmse     | 1.10133  |
| ogbg-mollipo | grover_base       | linear       | rmse     | 1.26927  |
| ogbg-mollipo | grover_large      | linear       | rmse     | 1.44984  |
| ogbg-mollipo | rmat_4M           | linear       | rmse     | 1.67961  |
| ogbg-mollipo | rmat_4M_rdkit     | linear       | rmse     | 4.27902  |

### ogbg-molmuv (classification)

| dataset     | base_model        | head_model   | metric   |     result |
|:------------|:------------------|:-------------|:---------|-----------:|
| ogbg-molmuv | mol2vec           | linear       | ap       | 0.0246996  |
| ogbg-molmuv | mat_masking_2M    | linear       | ap       | 0.00252069 |
| ogbg-molmuv | mat_masking_20M   | linear       | ap       | 0.00252069 |
| ogbg-molmuv | rmat_4M_rdkit     | linear       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-10M-MTR | linear       | ap       | 0.00252069 |
| ogbg-molmuv | rmat_4M           | linear       | ap       | 0.00252069 |
| ogbg-molmuv | mat_masking_200k  | linear       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-5M-MTR  | linear       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-77M-MTR | linear       | ap       | 0.00252069 |

### ogbg-molsider (classification)

| dataset       | base_model        | head_model   | metric   |   result |
|:--------------|:------------------|:-------------|:---------|---------:|
| ogbg-molsider | rmat_4M           | forest       | rocauc   | 0.672815 |
| ogbg-molsider | rmat_4M_rdkit     | forest       | rocauc   | 0.660948 |
| ogbg-molsider | mol2vec           | forest       | rocauc   | 0.653214 |
| ogbg-molsider | mat_masking_20M   | forest       | rocauc   | 0.647409 |
| ogbg-molsider | mat_masking_2M    | forest       | rocauc   | 0.645621 |
| ogbg-molsider | mat_masking_200k  | forest       | rocauc   | 0.642553 |
| ogbg-molsider | ChemBERTa-10M-MTR | forest       | rocauc   | 0.636374 |
| ogbg-molsider | ChemBERTa-77M-MTR | forest       | rocauc   | 0.632615 |
| ogbg-molsider | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.613488 |
| ogbg-molsider | ChemBERTa-10M-MTR | ridge        | rocauc   | 0.592574 |
| ogbg-molsider | ChemBERTa-77M-MTR | ridge        | rocauc   | 0.589305 |
| ogbg-molsider | mol2vec           | ridge        | rocauc   | 0.585859 |
| ogbg-molsider | ChemBERTa-5M-MTR  | ridge        | rocauc   | 0.573454 |
| ogbg-molsider | mat_masking_2M    | ridge        | rocauc   | 0.565926 |
| ogbg-molsider | rmat_4M           | linear       | rocauc   | 0.565157 |
| ogbg-molsider | grover_base       | forest       | rocauc   | 0.564759 |
| ogbg-molsider | grover_large      | forest       | rocauc   | 0.554998 |
| ogbg-molsider | rmat_4M_rdkit     | linear       | rocauc   | 0.548807 |
| ogbg-molsider | mat_masking_200k  | ridge        | rocauc   | 0.547454 |
| ogbg-molsider | rmat_4M_rdkit     | ridge        | rocauc   | 0.542247 |
| ogbg-molsider | grover_large      | ridge        | rocauc   | 0.541037 |
| ogbg-molsider | mat_masking_2M    | linear       | rocauc   | 0.540698 |
| ogbg-molsider | mol2vec           | linear       | rocauc   | 0.539678 |
| ogbg-molsider | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.538553 |
| ogbg-molsider | mat_masking_20M   | ridge        | rocauc   | 0.537213 |
| ogbg-molsider | ChemBERTa-77M-MTR | linear       | rocauc   | 0.536537 |
| ogbg-molsider | mat_masking_20M   | linear       | rocauc   | 0.533032 |
| ogbg-molsider | grover_base       | ridge        | rocauc   | 0.530186 |
| ogbg-molsider | mat_masking_200k  | linear       | rocauc   | 0.527033 |
| ogbg-molsider | grover_base       | linear       | rocauc   | 0.525398 |
| ogbg-molsider | rmat_4M           | ridge        | rocauc   | 0.521843 |
| ogbg-molsider | ChemBERTa-10M-MTR | linear       | rocauc   | 0.52021  |
| ogbg-molsider | grover_large      | linear       | rocauc   | 0.51919  |
| ogbg-molsider | molbert           | forest       | rocauc   | 0.506262 |

### ogbg-moltox21 (classification)

| dataset       | base_model        | head_model   | metric   |   result |
|:--------------|:------------------|:-------------|:---------|---------:|
| ogbg-moltox21 | ChemBERTa-10M-MTR | forest       | rocauc   | 0.768485 |
| ogbg-moltox21 | ChemBERTa-77M-MTR | forest       | rocauc   | 0.762444 |
| ogbg-moltox21 | mol2vec           | forest       | rocauc   | 0.760383 |
| ogbg-moltox21 | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.758756 |
| ogbg-moltox21 | mat_masking_200k  | ridge        | rocauc   | 0.737942 |
| ogbg-moltox21 | mol2vec           | ridge        | rocauc   | 0.726091 |
| ogbg-moltox21 | mat_masking_2M    | ridge        | rocauc   | 0.723276 |
| ogbg-moltox21 | ChemBERTa-5M-MTR  | ridge        | rocauc   | 0.721521 |
| ogbg-moltox21 | ChemBERTa-10M-MTR | ridge        | rocauc   | 0.718828 |
| ogbg-moltox21 | ChemBERTa-77M-MTR | ridge        | rocauc   | 0.716168 |
| ogbg-moltox21 | mat_masking_20M   | ridge        | rocauc   | 0.698871 |
| ogbg-moltox21 | rmat_4M           | ridge        | rocauc   | 0.664509 |
| ogbg-moltox21 | rmat_4M_rdkit     | ridge        | rocauc   | 0.634769 |
| ogbg-moltox21 | grover_base       | ridge        | rocauc   | 0.623224 |
| ogbg-moltox21 | grover_large      | ridge        | rocauc   | 0.615842 |
| ogbg-moltox21 | rmat_4M           | linear       | rocauc   | 0.610967 |
| ogbg-moltox21 | rmat_4M_rdkit     | linear       | rocauc   | 0.605261 |
| ogbg-moltox21 | mol2vec           | linear       | rocauc   | 0.603861 |
| ogbg-moltox21 | ChemBERTa-10M-MTR | linear       | rocauc   | 0.591052 |
| ogbg-moltox21 | mat_masking_2M    | linear       | rocauc   | 0.588861 |
| ogbg-moltox21 | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.582479 |
| ogbg-moltox21 | ChemBERTa-77M-MTR | linear       | rocauc   | 0.579727 |
| ogbg-moltox21 | mat_masking_20M   | linear       | rocauc   | 0.568553 |
| ogbg-moltox21 | grover_large      | linear       | rocauc   | 0.555958 |
| ogbg-moltox21 | mat_masking_200k  | linear       | rocauc   | 0.555659 |
| ogbg-moltox21 | grover_base       | linear       | rocauc   | 0.545108 |
| ogbg-moltox21 | molbert           | forest       | rocauc   | 0.538102 |

### ogbg-moltoxcast (classification)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| ogbg-moltoxcast | mat_masking_2M    | ridge        | rocauc   | 0.560541 |
| ogbg-moltoxcast | mat_masking_200k  | ridge        | rocauc   | 0.559336 |
| ogbg-moltoxcast | mat_masking_20M   | ridge        | rocauc   | 0.558755 |
| ogbg-moltoxcast | ChemBERTa-77M-MTR | ridge        | rocauc   | 0.554868 |
| ogbg-moltoxcast | mol2vec           | ridge        | rocauc   | 0.553646 |
| ogbg-moltoxcast | ChemBERTa-10M-MTR | ridge        | rocauc   | 0.553068 |
| ogbg-moltoxcast | ChemBERTa-5M-MTR  | ridge        | rocauc   | 0.549467 |
| ogbg-moltoxcast | rmat_4M_rdkit     | linear       | rocauc   | 0.519499 |
| ogbg-moltoxcast | rmat_4M           | linear       | rocauc   | 0.516141 |
| ogbg-moltoxcast | mol2vec           | linear       | rocauc   | 0.510599 |
| ogbg-moltoxcast | ChemBERTa-10M-MTR | linear       | rocauc   | 0.506748 |
| ogbg-moltoxcast | mat_masking_2M    | linear       | rocauc   | 0.504809 |
| ogbg-moltoxcast | grover_large      | linear       | rocauc   | 0.504284 |
| ogbg-moltoxcast | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.504098 |
| ogbg-moltoxcast | mat_masking_200k  | linear       | rocauc   | 0.503369 |
| ogbg-moltoxcast | mat_masking_20M   | linear       | rocauc   | 0.502762 |
| ogbg-moltoxcast | ChemBERTa-77M-MTR | linear       | rocauc   | 0.502633 |
| ogbg-moltoxcast | grover_base       | linear       | rocauc   | 0.501782 |

