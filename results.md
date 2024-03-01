### BBB_Martins (classification)

| dataset     | base_model        | head_model   | metric   |   result |
|:------------|:------------------|:-------------|:---------|---------:|
| BBB_Martins | **SOTA**          | nan          | roc-auc  |    0.92  |
| BBB_Martins | mat_masking_200k  | linear       | roc-auc  |    0.816 |
| BBB_Martins | mol2vec           | linear       | roc-auc  |    0.807 |
| BBB_Martins | mat_masking_2M    | linear       | roc-auc  |    0.784 |
| BBB_Martins | rmat_4M_rdkit     | linear       | roc-auc  |    0.784 |
| BBB_Martins | rmat_4M           | linear       | roc-auc  |    0.78  |
| BBB_Martins | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.778 |
| BBB_Martins | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.777 |
| BBB_Martins | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.774 |
| BBB_Martins | mat_masking_20M   | linear       | roc-auc  |    0.772 |
| BBB_Martins | rmat_4M           | forest       | roc-auc  |    0.758 |
| BBB_Martins | rmat_4M_rdkit     | forest       | roc-auc  |    0.754 |
| BBB_Martins | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.752 |
| BBB_Martins | mat_masking_200k  | forest       | roc-auc  |    0.751 |
| BBB_Martins | mol2vec           | forest       | roc-auc  |    0.736 |
| BBB_Martins | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.735 |
| BBB_Martins | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.734 |
| BBB_Martins | mat_masking_20M   | forest       | roc-auc  |    0.722 |
| BBB_Martins | grover_base       | linear       | roc-auc  |    0.692 |
| BBB_Martins | mat_masking_2M    | forest       | roc-auc  |    0.684 |
| BBB_Martins | grover_large      | linear       | roc-auc  |    0.67  |
| BBB_Martins | grover_large      | forest       | roc-auc  |    0.566 |
| BBB_Martins | grover_base       | forest       | roc-auc  |    0.545 |

### Bioavailability_Ma (classification)

| dataset            | base_model        | head_model   | metric   |   result |
|:-------------------|:------------------|:-------------|:---------|---------:|
| Bioavailability_Ma | **SOTA**          | nan          | rocauc   |    0.748 |
| Bioavailability_Ma | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.636 |
| Bioavailability_Ma | rmat_4M           | linear       | roc-auc  |    0.627 |
| Bioavailability_Ma | rmat_4M_rdkit     | forest       | roc-auc  |    0.619 |
| Bioavailability_Ma | rmat_4M_rdkit     | linear       | roc-auc  |    0.616 |
| Bioavailability_Ma | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.605 |
| Bioavailability_Ma | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.605 |
| Bioavailability_Ma | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.601 |
| Bioavailability_Ma | mol2vec           | linear       | roc-auc  |    0.596 |
| Bioavailability_Ma | mat_masking_2M    | linear       | roc-auc  |    0.593 |
| Bioavailability_Ma | mol2vec           | forest       | roc-auc  |    0.583 |
| Bioavailability_Ma | rmat_4M           | forest       | roc-auc  |    0.572 |
| Bioavailability_Ma | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.552 |
| Bioavailability_Ma | mat_masking_200k  | linear       | roc-auc  |    0.534 |
| Bioavailability_Ma | mat_masking_20M   | linear       | roc-auc  |    0.508 |
| Bioavailability_Ma | mat_masking_2M    | forest       | roc-auc  |    0.508 |
| Bioavailability_Ma | grover_large      | linear       | roc-auc  |    0.499 |
| Bioavailability_Ma | mat_masking_200k  | forest       | roc-auc  |    0.496 |
| Bioavailability_Ma | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.483 |
| Bioavailability_Ma | mat_masking_20M   | forest       | roc-auc  |    0.476 |
| Bioavailability_Ma | grover_large      | forest       | roc-auc  |    0.465 |
| Bioavailability_Ma | grover_base       | forest       | roc-auc  |    0.454 |
| Bioavailability_Ma | grover_base       | linear       | roc-auc  |    0.408 |

### CYP2C9_Substrate_CarbonMangels (classification)

| dataset                        | base_model        | head_model   | metric   |   result |
|:-------------------------------|:------------------|:-------------|:---------|---------:|
| CYP2C9_Substrate_CarbonMangels | **SOTA**          | nan          | pr-auc   |    0.441 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.372 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.347 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.337 |
| CYP2C9_Substrate_CarbonMangels | grover_large      | linear       | pr-auc   |    0.327 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M_rdkit     | forest       | pr-auc   |    0.318 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.3   |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.299 |
| CYP2C9_Substrate_CarbonMangels | grover_large      | forest       | pr-auc   |    0.293 
| CYP2C9_Substrate_CarbonMangels | mol2vec           | forest       | pr-auc   |    0.288 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_2M    | forest       | pr-auc   |    0.286 |
| CYP2C9_Substrate_CarbonMangels | mol2vec           | linear       | pr-auc   |    0.283 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_20M   | forest       | pr-auc   |    0.282 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_20M   | linear       | pr-auc   |    0.282 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_2M    | linear       | pr-auc   |    0.282 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M           | forest       | pr-auc   |    0.281 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_200k  | forest       | pr-auc   |    0.281 |
| CYP2C9_Substrate_CarbonMangels | mat_masking_200k  | linear       | pr-auc   |    0.281 |
| CYP2C9_Substrate_CarbonMangels | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.281 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M           | linear       | pr-auc   |    0.28  |
| CYP2C9_Substrate_CarbonMangels | grover_base       | forest       | pr-auc   |    0.278 |
| CYP2C9_Substrate_CarbonMangels | rmat_4M_rdkit     | linear       | pr-auc   |    0.277 |
| CYP2C9_Substrate_CarbonMangels | grover_base       | linear       | pr-auc   |    0.271 |

### CYP2C9_Veith (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| CYP2C9_Veith | **SOTA**          | nan          | pr-auc   |    0.859 |
| CYP2C9_Veith | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.582 |
| CYP2C9_Veith | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.579 |
| CYP2C9_Veith | rmat_4M           | linear       | pr-auc   |    0.574 |
| CYP2C9_Veith | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.573 |
| CYP2C9_Veith | mat_masking_2M    | linear       | pr-auc   |    0.572 |
| CYP2C9_Veith | mat_masking_200k  | linear       | pr-auc   |    0.56  |
| CYP2C9_Veith | rmat_4M_rdkit     | linear       | pr-auc   |    0.559 |
| CYP2C9_Veith | mat_masking_20M   | linear       | pr-auc   |    0.552 |
| CYP2C9_Veith | mat_masking_20M   | forest       | pr-auc   |    0.529 |
| CYP2C9_Veith | mol2vec           | linear       | pr-auc   |    0.529 |
| CYP2C9_Veith | mol2vec           | forest       | pr-auc   |    0.522 |
| CYP2C9_Veith | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.519 |
| CYP2C9_Veith | mat_masking_2M    | forest       | pr-auc   |    0.511 |
| CYP2C9_Veith | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.508 |
| CYP2C9_Veith | rmat_4M_rdkit     | forest       | pr-auc   |    0.505 |
| CYP2C9_Veith | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.498 |
| CYP2C9_Veith | mat_masking_200k  | forest       | pr-auc   |    0.498 |
| CYP2C9_Veith | grover_large      | linear       | pr-auc   |    0.497 |
| CYP2C9_Veith | grover_base       | linear       | pr-auc   |    0.493 |
| CYP2C9_Veith | rmat_4M           | forest       | pr-auc   |    0.488 |
| CYP2C9_Veith | grover_large      | forest       | pr-auc   |    0.368 |
| CYP2C9_Veith | grover_base       | forest       | pr-auc   |    0.362 |

### CYP2D6_Substrate_CarbonMangels (classification)

| dataset                        | base_model        | head_model   | metric   |   result |
|:-------------------------------|:------------------|:-------------|:---------|---------:|
| CYP2D6_Substrate_CarbonMangels | **SOTA**          | nan          | pr-auc   |    0.736 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M           | forest       | pr-auc   |    0.545 |
| CYP2D6_Substrate_CarbonMangels | mol2vec           | forest       | pr-auc   |    0.531 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_200k  | linear       | pr-auc   |    0.526 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.513 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.5   |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.493 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M_rdkit     | forest       | pr-auc   |    0.491 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_20M   | linear       | pr-auc   |    0.487 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.487 |
| CYP2D6_Substrate_CarbonMangels | mol2vec           | linear       | pr-auc   |    0.483 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M_rdkit     | linear       | pr-auc   |    0.481 |
| CYP2D6_Substrate_CarbonMangels | rmat_4M           | linear       | pr-auc   |    0.481 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_20M   | forest       | pr-auc   |    0.465 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_2M    | linear       | pr-auc   |    0.46  |
| CYP2D6_Substrate_CarbonMangels | mat_masking_2M    | forest       | pr-auc   |    0.451 |
| CYP2D6_Substrate_CarbonMangels | mat_masking_200k  | forest       | pr-auc   |    0.44  |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.436 |
| CYP2D6_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.432 |
| CYP2D6_Substrate_CarbonMangels | grover_large      | linear       | pr-auc   |    0.407 |
| CYP2D6_Substrate_CarbonMangels | grover_base       | linear       | pr-auc   |    0.383 |
| CYP2D6_Substrate_CarbonMangels | grover_base       | forest       | pr-auc   |    0.363 |
| CYP2D6_Substrate_CarbonMangels | grover_large      | forest       | pr-auc   |    0.318 |

### CYP2D6_Veith (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| CYP2D6_Veith | **SOTA**          | nan          | pr-auc   |    0.79  |
| CYP2D6_Veith | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.42  |
| CYP2D6_Veith | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.405 |
| CYP2D6_Veith | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.397 |
| CYP2D6_Veith | mat_masking_200k  | linear       | pr-auc   |    0.393 |
| CYP2D6_Veith | rmat_4M_rdkit     | linear       | pr-auc   |    0.384 |
| CYP2D6_Veith | mol2vec           | linear       | pr-auc   |    0.367 |
| CYP2D6_Veith | mat_masking_2M    | linear       | pr-auc   |    0.365 |
| CYP2D6_Veith | mat_masking_20M   | linear       | pr-auc   |    0.354 |
| CYP2D6_Veith | mat_masking_200k  | forest       | pr-auc   |    0.34  |
| CYP2D6_Veith | mat_masking_20M   | forest       | pr-auc   |    0.335 |
| CYP2D6_Veith | rmat_4M_rdkit     | forest       | pr-auc   |    0.326 |
| CYP2D6_Veith | mat_masking_2M    | forest       | pr-auc   |    0.325 |
| CYP2D6_Veith | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.324 |
| CYP2D6_Veith | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.302 |
| CYP2D6_Veith | grover_base       | linear       | pr-auc   |    0.299 |
| CYP2D6_Veith | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.295 |
| CYP2D6_Veith | mol2vec           | forest       | pr-auc   |    0.284 |
| CYP2D6_Veith | grover_large      | linear       | pr-auc   |    0.282 |
| CYP2D6_Veith | grover_large      | forest       | pr-auc   |    0.172 |
| CYP2D6_Veith | grover_base       | forest       | pr-auc   |    0.172 |

### CYP3A4_Substrate_CarbonMangels (classification)

| dataset                        | base_model        | head_model   | metric   |   result |
|:-------------------------------|:------------------|:-------------|:---------|---------:|
| CYP3A4_Substrate_CarbonMangels | **SOTA**          | nan          | roc-auc  |    0.667 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.646 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.634 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.631 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.629 |
| CYP3A4_Substrate_CarbonMangels | mol2vec           | linear       | roc-auc  |    0.624 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_2M    | linear       | roc-auc  |    0.616 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_20M   | linear       | roc-auc  |    0.613 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_200k  | linear       | roc-auc  |    0.604 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_20M   | forest       | roc-auc  |    0.599 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.596 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M           | forest       | roc-auc  |    0.584 |
| CYP3A4_Substrate_CarbonMangels | grover_base       | linear       | roc-auc  |    0.582 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_2M    | forest       | roc-auc  |    0.581 |
| CYP3A4_Substrate_CarbonMangels | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.57  |
| CYP3A4_Substrate_CarbonMangels | mol2vec           | forest       | roc-auc  |    0.569 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M           | linear       | roc-auc  |    0.564 |
| CYP3A4_Substrate_CarbonMangels | mat_masking_200k  | forest       | roc-auc  |    0.552 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M_rdkit     | linear       | roc-auc  |    0.541 |
| CYP3A4_Substrate_CarbonMangels | grover_large      | linear       | roc-auc  |    0.536 |
| CYP3A4_Substrate_CarbonMangels | grover_base       | forest       | roc-auc  |    0.532 |
| CYP3A4_Substrate_CarbonMangels | rmat_4M_rdkit     | forest       | roc-auc  |    0.528 |
| CYP3A4_Substrate_CarbonMangels | grover_large      | forest       | roc-auc  |    0.485 |

### CYP3A4_Veith (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| CYP3A4_Veith | **SOTA**          | nan          | pr-auc   |    0.916 |
| CYP3A4_Veith | rmat_4M           | linear       | pr-auc   |    0.677 |
| CYP3A4_Veith | ChemBERTa-5M-MTR  | linear       | pr-auc   |    0.671 |
| CYP3A4_Veith | ChemBERTa-77M-MTR | linear       | pr-auc   |    0.67  |
| CYP3A4_Veith | rmat_4M_rdkit     | linear       | pr-auc   |    0.665 |
| CYP3A4_Veith | mat_masking_2M    | linear       | pr-auc   |    0.663 |
| CYP3A4_Veith | ChemBERTa-10M-MTR | linear       | pr-auc   |    0.662 |
| CYP3A4_Veith | mat_masking_200k  | linear       | pr-auc   |    0.658 |
| CYP3A4_Veith | mat_masking_20M   | linear       | pr-auc   |    0.651 |
| CYP3A4_Veith | mol2vec           | linear       | pr-auc   |    0.645 |
| CYP3A4_Veith | ChemBERTa-10M-MTR | forest       | pr-auc   |    0.631 |
| CYP3A4_Veith | mat_masking_20M   | forest       | pr-auc   |    0.629 |
| CYP3A4_Veith | mat_masking_2M    | forest       | pr-auc   |    0.627 |
| CYP3A4_Veith | rmat_4M_rdkit     | forest       | pr-auc   |    0.623 |
| CYP3A4_Veith | ChemBERTa-77M-MTR | forest       | pr-auc   |    0.62  |
| CYP3A4_Veith | mat_masking_200k  | forest       | pr-auc   |    0.612 |
| CYP3A4_Veith | rmat_4M           | forest       | pr-auc   |    0.608 |
| CYP3A4_Veith | ChemBERTa-5M-MTR  | forest       | pr-auc   |    0.607 |
| CYP3A4_Veith | mol2vec           | forest       | pr-auc   |    0.603 |
| CYP3A4_Veith | grover_large      | linear       | pr-auc   |    0.586 |
| CYP3A4_Veith | grover_base       | linear       | pr-auc   |    0.574 |
| CYP3A4_Veith | grover_large      | forest       | pr-auc   |    0.505 |
| CYP3A4_Veith | grover_base       | forest       | pr-auc   |    0.497 |

### Caco2_Wang (regression)

| dataset    | base_model        | head_model   | metric   |   result |
|:-----------|:------------------|:-------------|:---------|---------:|
| Caco2_Wang | **SOTA**          | nan          | mae      |    0.276 |
| Caco2_Wang | rmat_4M_rdkit     | forest       | mae      |    0.314 |
| Caco2_Wang | mol2vec           | forest       | mae      |    0.326 |
| Caco2_Wang | mat_masking_20M   | forest       | mae      |    0.331 |
| Caco2_Wang | ChemBERTa-5M-MTR  | forest       | mae      |    0.343 |
| Caco2_Wang | rmat_4M           | forest       | mae      |    0.345 |
| Caco2_Wang | ChemBERTa-10M-MTR | forest       | mae      |    0.354 |
| Caco2_Wang | ChemBERTa-77M-MTR | forest       | mae      |    0.358 |
| Caco2_Wang | mat_masking_2M    | forest       | mae      |    0.36  |
| Caco2_Wang | mat_masking_200k  | forest       | mae      |    0.381 |
| Caco2_Wang | ChemBERTa-77M-MTR | linear       | mae      |    0.437 |
| Caco2_Wang | ChemBERTa-10M-MTR | linear       | mae      |    0.45  |
| Caco2_Wang | grover_large      | forest       | mae      |    0.494 |
| Caco2_Wang | grover_base       | forest       | mae      |    0.513 |
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
| Clearance_Hepatocyte_AZ | **SOTA**          | nan          | spearman |    0.536 |
| Clearance_Hepatocyte_AZ | rmat_4M_rdkit     | forest       | spearman |    0.323 |
| Clearance_Hepatocyte_AZ | ChemBERTa-77M-MTR | forest       | spearman |    0.298 |
| Clearance_Hepatocyte_AZ | mol2vec           | linear       | spearman |    0.298 |
| Clearance_Hepatocyte_AZ | mol2vec           | forest       | spearman |    0.29  |
| Clearance_Hepatocyte_AZ | ChemBERTa-10M-MTR | forest       | spearman |    0.287 |
| Clearance_Hepatocyte_AZ | grover_base       | linear       | spearman |    0.286 |
| Clearance_Hepatocyte_AZ | mat_masking_20M   | forest       | spearman |    0.253 |
| Clearance_Hepatocyte_AZ | mat_masking_200k  | forest       | spearman |    0.247 |
| Clearance_Hepatocyte_AZ | mat_masking_2M    | forest       | spearman |    0.234 |
| Clearance_Hepatocyte_AZ | ChemBERTa-77M-MTR | linear       | spearman |    0.224 |
| Clearance_Hepatocyte_AZ | ChemBERTa-5M-MTR  | forest       | spearman |    0.223 |
| Clearance_Hepatocyte_AZ | ChemBERTa-10M-MTR | linear       | spearman |    0.213 |
| Clearance_Hepatocyte_AZ | mat_masking_200k  | linear       | spearman |    0.205 |
| Clearance_Hepatocyte_AZ | rmat_4M           | forest       | spearman |    0.198 |
| Clearance_Hepatocyte_AZ | ChemBERTa-5M-MTR  | linear       | spearman |    0.185 |
| Clearance_Hepatocyte_AZ | mat_masking_2M    | linear       | spearman |    0.143 |
| Clearance_Hepatocyte_AZ | grover_large      | linear       | spearman |    0.083 |
| Clearance_Hepatocyte_AZ | rmat_4M           | linear       | spearman |    0.073 |
| Clearance_Hepatocyte_AZ | mat_masking_20M   | linear       | spearman |    0.044 |
| Clearance_Hepatocyte_AZ | grover_base       | forest       | spearman |    0.041 |
| Clearance_Hepatocyte_AZ | grover_large      | forest       | spearman |   -0.011 |
| Clearance_Hepatocyte_AZ | rmat_4M_rdkit     | linear       | spearman |   -0.059 |

### HIA_Hou (classification)

| dataset   | base_model        | head_model   | metric   |   result |
|:----------|:------------------|:-------------|:---------|---------:|
| HIA_Hou   | **SOTA**          | nan          | roc-auc  |    0.989 |
| HIA_Hou   | rmat_4M_rdkit     | linear       | roc-auc  |    0.933 |
| HIA_Hou   | rmat_4M           | linear       | roc-auc  |    0.933 |
| HIA_Hou   | mol2vec           | linear       | roc-auc  |    0.917 |
| HIA_Hou   | mat_masking_20M   | linear       | roc-auc  |    0.902 |
| HIA_Hou   | mat_masking_2M    | linear       | roc-auc  |    0.891 |
| HIA_Hou   | mat_masking_200k  | linear       | roc-auc  |    0.867 |
| HIA_Hou   | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.859 |
| HIA_Hou   | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.843 |
| HIA_Hou   | mat_masking_20M   | forest       | roc-auc  |    0.835 |
| HIA_Hou   | mat_masking_2M    | forest       | roc-auc  |    0.822 |
| HIA_Hou   | mol2vec           | forest       | roc-auc  |    0.822 |
| HIA_Hou   | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.817 |
| HIA_Hou   | rmat_4M           | forest       | roc-auc  |    0.809 |
| HIA_Hou   | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.791 |
| HIA_Hou   | rmat_4M_rdkit     | forest       | roc-auc  |    0.778 |
| HIA_Hou   | mat_masking_200k  | forest       | roc-auc  |    0.774 |
| HIA_Hou   | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.706 |
| HIA_Hou   | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.704 |
| HIA_Hou   | grover_large      | linear       | roc-auc  |    0.676 |
| HIA_Hou   | grover_base       | linear       | roc-auc  |    0.672 |
| HIA_Hou   | grover_large      | forest       | roc-auc  |    0.626 |
| HIA_Hou   | grover_base       | forest       | roc-auc  |    0.565 |

### Half_Life_Obach (regression)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| Half_Life_Obach | **SOTA**          | nan          | spearman |    0.576 |
| Half_Life_Obach | mol2vec           | forest       | spearman |    0.37  |
| Half_Life_Obach | rmat_4M_rdkit     | forest       | spearman |    0.345 |
| Half_Life_Obach | mat_masking_20M   | forest       | spearman |    0.293 |
| Half_Life_Obach | mat_masking_2M    | forest       | spearman |    0.287 |
| Half_Life_Obach | ChemBERTa-5M-MTR  | forest       | spearman |    0.267 |
| Half_Life_Obach | rmat_4M           | forest       | spearman |    0.246 |
| Half_Life_Obach | mat_masking_200k  | forest       | spearman |    0.246 |
| Half_Life_Obach | ChemBERTa-77M-MTR | forest       | spearman |    0.208 |
| Half_Life_Obach | ChemBERTa-10M-MTR | forest       | spearman |    0.203 |
| Half_Life_Obach | mat_masking_200k  | linear       | spearman |    0.144 |
| Half_Life_Obach | ChemBERTa-5M-MTR  | linear       | spearman |    0.115 |
| Half_Life_Obach | rmat_4M_rdkit     | linear       | spearman |    0.11  |
| Half_Life_Obach | mat_masking_20M   | linear       | spearman |    0.092 |
| Half_Life_Obach | grover_base       | linear       | spearman |    0.081 |
| Half_Life_Obach | mat_masking_2M    | linear       | spearman |    0.078 |
| Half_Life_Obach | mol2vec           | linear       | spearman |    0.047 |
| Half_Life_Obach | grover_large      | linear       | spearman |    0.044 |
| Half_Life_Obach | grover_large      | forest       | spearman |    0.04  |
| Half_Life_Obach | rmat_4M           | linear       | spearman |    0.037 |
| Half_Life_Obach | ChemBERTa-77M-MTR | linear       | spearman |    0.019 |
| Half_Life_Obach | grover_base       | forest       | spearman |   -0.002 |
| Half_Life_Obach | ChemBERTa-10M-MTR | linear       | spearman |   -0.021 |

### Lipophilicity_AstraZeneca (regression)

| dataset                   | base_model        | head_model   | metric   |   result |
|:--------------------------|:------------------|:-------------|:---------|---------:|
| Lipophilicity_AstraZeneca | **SOTA**          | nan          | mae      |    0.467 |
| Lipophilicity_AstraZeneca | ChemBERTa-77M-MTR | linear       | mae      |    0.598 |
| Lipophilicity_AstraZeneca | ChemBERTa-10M-MTR | linear       | mae      |    0.603 |
| Lipophilicity_AstraZeneca | mat_masking_2M    | linear       | mae      |    0.604 |
| Lipophilicity_AstraZeneca | mat_masking_200k  | linear       | mae      |    0.609 |
| Lipophilicity_AstraZeneca | mat_masking_20M   | linear       | mae      |    0.61  |
| Lipophilicity_AstraZeneca | ChemBERTa-5M-MTR  | linear       | mae      |    0.619 |
| Lipophilicity_AstraZeneca | mol2vec           | linear       | mae      |    0.659 |
| Lipophilicity_AstraZeneca | rmat_4M_rdkit     | forest       | mae      |    0.691 |
| Lipophilicity_AstraZeneca | ChemBERTa-10M-MTR | forest       | mae      |    0.708 |
| Lipophilicity_AstraZeneca | ChemBERTa-5M-MTR  | forest       | mae      |    0.731 |
| Lipophilicity_AstraZeneca | mat_masking_2M    | forest       | mae      |    0.742 |
| Lipophilicity_AstraZeneca | rmat_4M           | forest       | mae      |    0.744 |
| Lipophilicity_AstraZeneca | ChemBERTa-77M-MTR | forest       | mae      |    0.748 |
| Lipophilicity_AstraZeneca | mat_masking_20M   | forest       | mae      |    0.752 |
| Lipophilicity_AstraZeneca | mat_masking_200k  | forest       | mae      |    0.757 |
| Lipophilicity_AstraZeneca | mol2vec           | forest       | mae      |    0.811 |
| Lipophilicity_AstraZeneca | grover_large      | forest       | mae      |    0.977 |
| Lipophilicity_AstraZeneca | grover_base       | forest       | mae      |    1.006 |
| Lipophilicity_AstraZeneca | grover_base       | linear       | mae      |    1.019 |
| Lipophilicity_AstraZeneca | grover_large      | linear       | mae      |    1.333 |
| Lipophilicity_AstraZeneca | rmat_4M           | linear       | mae      |    1.668 |
| Lipophilicity_AstraZeneca | rmat_4M_rdkit     | linear       | mae      |    2.935 |

### Pgp_Broccatelli (classification)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| Pgp_Broccatelli | **SOTA**          | nan          | roc-auc  |    0.938 |
| Pgp_Broccatelli | mat_masking_2M    | forest       | roc-auc  |    0.865 |
| Pgp_Broccatelli | mat_masking_200k  | linear       | roc-auc  |    0.849 |
| Pgp_Broccatelli | mat_masking_2M    | linear       | roc-auc  |    0.849 |
| Pgp_Broccatelli | ChemBERTa-10M-MTR | linear       | roc-auc  |    0.833 |
| Pgp_Broccatelli | mat_masking_20M   | forest       | roc-auc  |    0.821 |
| Pgp_Broccatelli | ChemBERTa-77M-MTR | linear       | roc-auc  |    0.813 |
| Pgp_Broccatelli | rmat_4M           | forest       | roc-auc  |    0.809 |
| Pgp_Broccatelli | mat_masking_20M   | linear       | roc-auc  |    0.808 |
| Pgp_Broccatelli | mol2vec           | linear       | roc-auc  |    0.804 |
| Pgp_Broccatelli | mat_masking_200k  | forest       | roc-auc  |    0.8   |
| Pgp_Broccatelli | ChemBERTa-5M-MTR  | forest       | roc-auc  |    0.797 |
| Pgp_Broccatelli | ChemBERTa-5M-MTR  | linear       | roc-auc  |    0.792 |
| Pgp_Broccatelli | rmat_4M_rdkit     | forest       | roc-auc  |    0.785 |
| Pgp_Broccatelli | ChemBERTa-10M-MTR | forest       | roc-auc  |    0.776 |
| Pgp_Broccatelli | mol2vec           | forest       | roc-auc  |    0.773 |
| Pgp_Broccatelli | ChemBERTa-77M-MTR | forest       | roc-auc  |    0.757 |
| Pgp_Broccatelli | rmat_4M           | linear       | roc-auc  |    0.751 |
| Pgp_Broccatelli | rmat_4M_rdkit     | linear       | roc-auc  |    0.747 |
| Pgp_Broccatelli | grover_base       | linear       | roc-auc  |    0.738 |
| Pgp_Broccatelli | grover_large      | linear       | roc-auc  |    0.702 |
| Pgp_Broccatelli | grover_large      | forest       | roc-auc  |    0.669 |
| Pgp_Broccatelli | grover_base       | forest       | roc-auc  |    0.656 |

### Solubility_AqSolDB (regression)

| dataset            | base_model        | head_model   | metric   |   result |
|:-------------------|:------------------|:-------------|:---------|---------:|
| Solubility_AqSolDB | **SOTA**          | nan          | mae      |    0.761 |
| Solubility_AqSolDB | rmat_4M_rdkit     | forest       | mae      |    0.869 |
| Solubility_AqSolDB | mat_masking_20M   | linear       | mae      |    0.871 |
| Solubility_AqSolDB | mat_masking_200k  | linear       | mae      |    0.885 |
| Solubility_AqSolDB | mat_masking_2M    | linear       | mae      |    0.904 |
| Solubility_AqSolDB | ChemBERTa-10M-MTR | linear       | mae      |    0.951 |
| Solubility_AqSolDB | ChemBERTa-77M-MTR | linear       | mae      |    0.965 |
| Solubility_AqSolDB | mat_masking_2M    | forest       | mae      |    0.993 |
| Solubility_AqSolDB | rmat_4M           | forest       | mae      |    1.003 |
| Solubility_AqSolDB | mat_masking_20M   | forest       | mae      |    1.015 |
| Solubility_AqSolDB | ChemBERTa-10M-MTR | forest       | mae      |    1.02  |
| Solubility_AqSolDB | ChemBERTa-5M-MTR  | linear       | mae      |    1.021 |
| Solubility_AqSolDB | ChemBERTa-5M-MTR  | forest       | mae      |    1.029 |
| Solubility_AqSolDB | ChemBERTa-77M-MTR | forest       | mae      |    1.029 |
| Solubility_AqSolDB | mat_masking_200k  | forest       | mae      |    1.04  |
| Solubility_AqSolDB | mol2vec           | forest       | mae      |    1.052 |
| Solubility_AqSolDB | rmat_4M           | linear       | mae      |    1.119 |
| Solubility_AqSolDB | rmat_4M_rdkit     | linear       | mae      |    1.134 |
| Solubility_AqSolDB | mol2vec           | linear       | mae      |    1.164 |
| Solubility_AqSolDB | grover_base       | linear       | mae      |    1.252 |
| Solubility_AqSolDB | grover_large      | linear       | mae      |    1.342 |
| Solubility_AqSolDB | grover_large      | forest       | mae      |    1.423 |
| Solubility_AqSolDB | grover_base       | forest       | mae      |    1.498 |

### VDss_Lombardo (regression)

| dataset       | base_model        | head_model   | metric   |   result |
|:--------------|:------------------|:-------------|:---------|---------:|
| VDss_Lombardo | **SOTA**          | nan          | spearman |    0.713 |
| VDss_Lombardo | mat_masking_2M    | forest       | spearman |    0.478 |
| VDss_Lombardo | mat_masking_20M   | forest       | spearman |    0.468 |
| VDss_Lombardo | rmat_4M_rdkit     | forest       | spearman |    0.43  |
| VDss_Lombardo | ChemBERTa-10M-MTR | forest       | spearman |    0.411 |
| VDss_Lombardo | mat_masking_200k  | forest       | spearman |    0.409 |
| VDss_Lombardo | rmat_4M           | forest       | spearman |    0.399 |
| VDss_Lombardo | mol2vec           | forest       | spearman |    0.381 |
| VDss_Lombardo | ChemBERTa-77M-MTR | forest       | spearman |    0.373 |
| VDss_Lombardo | ChemBERTa-10M-MTR | linear       | spearman |    0.284 |
| VDss_Lombardo | ChemBERTa-5M-MTR  | forest       | spearman |    0.262 |
| VDss_Lombardo | grover_large      | forest       | spearman |    0.179 |
| VDss_Lombardo | ChemBERTa-77M-MTR | linear       | spearman |    0.149 |
| VDss_Lombardo | mol2vec           | linear       | spearman |    0.136 |
| VDss_Lombardo | grover_base       | forest       | spearman |    0.081 |
| VDss_Lombardo | mat_masking_20M   | linear       | spearman |    0.07  |
| VDss_Lombardo | grover_base       | linear       | spearman |    0.054 |
| VDss_Lombardo | rmat_4M           | linear       | spearman |    0.048 |
| VDss_Lombardo | mat_masking_200k  | linear       | spearman |    0.044 |
| VDss_Lombardo | rmat_4M_rdkit     | linear       | spearman |    0.043 |
| VDss_Lombardo | mat_masking_2M    | linear       | spearman |    0.04  |
| VDss_Lombardo | grover_large      | linear       | spearman |    0.03  |
| VDss_Lombardo | ChemBERTa-5M-MTR  | linear       | spearman |   -0.014 |

### ogbg-molbace (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| ogbg-molbace | mat_masking_20M   | linear       | rocauc   | 0.683533 |
| ogbg-molbace | mat_masking_2M    | forest       | rocauc   | 0.682664 |
| ogbg-molbace | rmat_4M           | forest       | rocauc   | 0.670318 |
| ogbg-molbace | ChemBERTa-10M-MTR | forest       | rocauc   | 0.669449 |
| ogbg-molbace | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.66771  |
| ogbg-molbace | mol2vec           | forest       | rocauc   | 0.66771  |
| ogbg-molbace | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.666841 |
| ogbg-molbace | rmat_4M           | linear       | rocauc   | 0.665971 |
| ogbg-molbace | ChemBERTa-77M-MTR | forest       | rocauc   | 0.665015 |
| ogbg-molbace | rmat_4M_rdkit     | forest       | rocauc   | 0.665015 |
| ogbg-molbace | ChemBERTa-10M-MTR | linear       | rocauc   | 0.664145 |
| ogbg-molbace | mat_masking_2M    | linear       | rocauc   | 0.663276 |
| ogbg-molbace | ChemBERTa-77M-MTR | linear       | rocauc   | 0.662407 |
| ogbg-molbace | mat_masking_200k  | forest       | rocauc   | 0.660581 |
| ogbg-molbace | mat_masking_20M   | forest       | rocauc   | 0.660581 |
| ogbg-molbace | mat_masking_200k  | linear       | rocauc   | 0.645627 |
| ogbg-molbace | rmat_4M_rdkit     | linear       | rocauc   | 0.61485  |
| ogbg-molbace | mol2vec           | linear       | rocauc   | 0.609546 |
| ogbg-molbace | grover_base       | linear       | rocauc   | 0.587463 |
| ogbg-molbace | grover_large      | linear       | rocauc   | 0.546166 |
| ogbg-molbace | grover_base       | forest       | rocauc   | 0.535472 |
| ogbg-molbace | grover_large      | forest       | rocauc   | 0.535472 |

### ogbg-molbbbp (classification)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| ogbg-molbbbp | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.668981 |
| ogbg-molbbbp | ChemBERTa-77M-MTR | linear       | rocauc   | 0.659144 |
| ogbg-molbbbp | rmat_4M_rdkit     | linear       | rocauc   | 0.656829 |
| ogbg-molbbbp | ChemBERTa-10M-MTR | linear       | rocauc   | 0.633681 |
| ogbg-molbbbp | rmat_4M           | linear       | rocauc   | 0.632523 |
| ogbg-molbbbp | ChemBERTa-10M-MTR | forest       | rocauc   | 0.623264 |
| ogbg-molbbbp | mat_masking_2M    | linear       | rocauc   | 0.59838  |
| ogbg-molbbbp | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.596065 |
| ogbg-molbbbp | mol2vec           | linear       | rocauc   | 0.594329 |
| ogbg-molbbbp | rmat_4M_rdkit     | forest       | rocauc   | 0.589699 |
| ogbg-molbbbp | grover_large      | linear       | rocauc   | 0.583333 |
| ogbg-molbbbp | rmat_4M           | forest       | rocauc   | 0.581597 |
| ogbg-molbbbp | ChemBERTa-77M-MTR | forest       | rocauc   | 0.581019 |
| ogbg-molbbbp | mat_masking_200k  | linear       | rocauc   | 0.578125 |
| ogbg-molbbbp | grover_base       | linear       | rocauc   | 0.576389 |
| ogbg-molbbbp | mat_masking_2M    | forest       | rocauc   | 0.571759 |
| ogbg-molbbbp | mat_masking_20M   | linear       | rocauc   | 0.566551 |
| ogbg-molbbbp | mat_masking_20M   | forest       | rocauc   | 0.560185 |
| ogbg-molbbbp | mol2vec           | forest       | rocauc   | 0.556713 |
| ogbg-molbbbp | mat_masking_200k  | forest       | rocauc   | 0.540509 |
| ogbg-molbbbp | grover_base       | forest       | rocauc   | 0.49537  |
| ogbg-molbbbp | grover_large      | forest       | rocauc   | 0.475694 |

### ogbg-molclintox (classification)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| ogbg-molclintox | ChemBERTa-10M-MTR | linear       | rocauc   | 0.892646 |
| ogbg-molclintox | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.890834 |
| ogbg-molclintox | ChemBERTa-77M-MTR | linear       | rocauc   | 0.838057 |
| ogbg-molclintox | ChemBERTa-77M-MTR | forest       | rocauc   | 0.806682 |
| ogbg-molclintox | mol2vec           | linear       | rocauc   | 0.791085 |
| ogbg-molclintox | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.785279 |
| ogbg-molclintox | rmat_4M_rdkit     | linear       | rocauc   | 0.755689 |
| ogbg-molclintox | rmat_4M           | linear       | rocauc   | 0.752079 |
| ogbg-molclintox | mat_masking_2M    | linear       | rocauc   | 0.747637 |
| ogbg-molclintox | ChemBERTa-10M-MTR | forest       | rocauc   | 0.730715 |
| ogbg-molclintox | mat_masking_20M   | linear       | rocauc   | 0.700281 |
| ogbg-molclintox | mat_masking_200k  | linear       | rocauc   | 0.69306  |
| ogbg-molclintox | grover_large      | linear       | rocauc   | 0.587247 |
| ogbg-molclintox | grover_base       | linear       | rocauc   | 0.564045 |
| ogbg-molclintox | mat_masking_20M   | forest       | rocauc   | 0.547382 |
| ogbg-molclintox | mat_masking_2M    | forest       | rocauc   | 0.546524 |
| ogbg-molclintox | mat_masking_200k  | forest       | rocauc   | 0.545571 |
| ogbg-molclintox | rmat_4M_rdkit     | forest       | rocauc   | 0.523188 |
| ogbg-molclintox | rmat_4M           | forest       | rocauc   | 0.5      |
| ogbg-molclintox | mol2vec           | forest       | rocauc   | 0.5      |
| ogbg-molclintox | grover_base       | forest       | rocauc   | 0.49639  |
| ogbg-molclintox | grover_large      | forest       | rocauc   | 0.494578 |

### ogbg-molesol (regression)

| dataset      | base_model        | head_model   | metric   |     result |
|:-------------|:------------------|:-------------|:---------|-----------:|
| ogbg-molesol | rmat_4M_rdkit     | forest       | rmse     |   0.8261   |
| ogbg-molesol | ChemBERTa-10M-MTR | forest       | rmse     |   0.932427 |
| ogbg-molesol | mat_masking_20M   | forest       | rmse     |   0.961894 |
| ogbg-molesol | mat_masking_2M    | forest       | rmse     |   0.968184 |
| ogbg-molesol | rmat_4M           | forest       | rmse     |   1.01359  |
| ogbg-molesol | mat_masking_200k  | forest       | rmse     |   1.06219  |
| ogbg-molesol | ChemBERTa-5M-MTR  | forest       | rmse     |   1.10099  |
| ogbg-molesol | ChemBERTa-77M-MTR | forest       | rmse     |   1.113    |
| ogbg-molesol | mol2vec           | forest       | rmse     |   1.1342   |
| ogbg-molesol | ChemBERTa-10M-MTR | linear       | rmse     |   1.35933  |
| ogbg-molesol | ChemBERTa-5M-MTR  | linear       | rmse     |   1.58274  |
| ogbg-molesol | mol2vec           | linear       | rmse     |   1.60867  |
| ogbg-molesol | ChemBERTa-77M-MTR | linear       | rmse     |   1.63884  |
| ogbg-molesol | grover_large      | forest       | rmse     |   1.66699  |
| ogbg-molesol | grover_base       | forest       | rmse     |   1.88412  |
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
| ogbg-molfreesolv | mat_masking_20M   | forest       | rmse     |  2.16738 |
| ogbg-molfreesolv | mat_masking_2M    | forest       | rmse     |  2.25702 |
| ogbg-molfreesolv | ChemBERTa-10M-MTR | forest       | rmse     |  2.26351 |
| ogbg-molfreesolv | ChemBERTa-5M-MTR  | forest       | rmse     |  2.29399 |
| ogbg-molfreesolv | rmat_4M_rdkit     | forest       | rmse     |  2.36348 |
| ogbg-molfreesolv | mat_masking_200k  | forest       | rmse     |  2.3864  |
| ogbg-molfreesolv | rmat_4M           | linear       | rmse     |  2.45472 |
| ogbg-molfreesolv | rmat_4M_rdkit     | linear       | rmse     |  2.47985 |
| ogbg-molfreesolv | rmat_4M           | forest       | rmse     |  2.89852 |
| ogbg-molfreesolv | grover_base       | forest       | rmse     |  3.20396 |
| ogbg-molfreesolv | ChemBERTa-77M-MTR | forest       | rmse     |  3.33085 |
| ogbg-molfreesolv | grover_large      | forest       | rmse     |  3.40879 |
| ogbg-molfreesolv | mol2vec           | forest       | rmse     |  3.49469 |
| ogbg-molfreesolv | grover_large      | linear       | rmse     |  3.50614 |
| ogbg-molfreesolv | grover_base       | linear       | rmse     |  3.9148  |
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
| ogbg-molhiv | **SOTA**          | nan          | rocauc   | 0.8475   |
| ogbg-molhiv | mol2vec           | forest       | rocauc   | 0.575291 |
| ogbg-molhiv | mol2vec           | linear       | rocauc   | 0.574538 |
| ogbg-molhiv | ChemBERTa-77M-MTR | linear       | rocauc   | 0.571445 |
| ogbg-molhiv | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.567975 |
| ogbg-molhiv | ChemBERTa-77M-MTR | forest       | rocauc   | 0.567599 |
| ogbg-molhiv | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.563753 |
| ogbg-molhiv | ChemBERTa-10M-MTR | forest       | rocauc   | 0.560032 |
| ogbg-molhiv | ChemBERTa-10M-MTR | linear       | rocauc   | 0.556311 |
| ogbg-molhiv | grover_large      | linear       | rocauc   | 0.5357   |
| ogbg-molhiv | grover_base       | linear       | rocauc   | 0.518352 |
| ogbg-molhiv | grover_large      | forest       | rocauc   | 0.507316 |
| ogbg-molhiv | grover_base       | forest       | rocauc   | 0.499121 |

### ogbg-mollipo (regression)

| dataset      | base_model        | head_model   | metric   |   result |
|:-------------|:------------------|:-------------|:---------|---------:|
| ogbg-mollipo | ChemBERTa-5M-MTR  | linear       | rmse     | 0.795198 |
| ogbg-mollipo | ChemBERTa-77M-MTR | linear       | rmse     | 0.806851 |
| ogbg-mollipo | mat_masking_2M    | linear       | rmse     | 0.809546 |
| ogbg-mollipo | rmat_4M_rdkit     | forest       | rmse     | 0.820876 |
| ogbg-mollipo | ChemBERTa-10M-MTR | linear       | rmse     | 0.85315  |
| ogbg-mollipo | mat_masking_20M   | forest       | rmse     | 0.858101 |
| ogbg-mollipo | mat_masking_200k  | linear       | rmse     | 0.870232 |
| ogbg-mollipo | mat_masking_20M   | linear       | rmse     | 0.875111 |
| ogbg-mollipo | mat_masking_200k  | forest       | rmse     | 0.879541 |
| ogbg-mollipo | ChemBERTa-10M-MTR | forest       | rmse     | 0.885533 |
| ogbg-mollipo | mol2vec           | linear       | rmse     | 0.896467 |
| ogbg-mollipo | mat_masking_2M    | forest       | rmse     | 0.898909 |
| ogbg-mollipo | rmat_4M           | forest       | rmse     | 0.899879 |
| ogbg-mollipo | ChemBERTa-5M-MTR  | forest       | rmse     | 0.92055  |
| ogbg-mollipo | ChemBERTa-77M-MTR | forest       | rmse     | 0.930757 |
| ogbg-mollipo | mol2vec           | forest       | rmse     | 0.953584 |
| ogbg-mollipo | grover_base       | forest       | rmse     | 1.12756  |
| ogbg-mollipo | grover_large      | forest       | rmse     | 1.14655  |
| ogbg-mollipo | grover_base       | linear       | rmse     | 1.26927  |
| ogbg-mollipo | grover_large      | linear       | rmse     | 1.44984  |
| ogbg-mollipo | rmat_4M           | linear       | rmse     | 1.67961  |
| ogbg-mollipo | rmat_4M_rdkit     | linear       | rmse     | 4.27902  |

### ogbg-molmuv (classification)

| dataset     | base_model        | head_model   | metric   |     result |
|:------------|:------------------|:-------------|:---------|-----------:|
| ogbg-molmuv | mol2vec           | linear       | ap       | 0.0246996  |
| ogbg-molmuv | mat_masking_20M   | linear       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-10M-MTR | forest       | ap       | 0.00252069 |
| ogbg-molmuv | rmat_4M           | forest       | ap       | 0.00252069 |
| ogbg-molmuv | rmat_4M_rdkit     | linear       | ap       | 0.00252069 |
| ogbg-molmuv | rmat_4M_rdkit     | forest       | ap       | 0.00252069 |
| ogbg-molmuv | rmat_4M           | linear       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-77M-MTR | forest       | ap       | 0.00252069 |
| ogbg-molmuv | mat_masking_2M    | linear       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-77M-MTR | linear       | ap       | 0.00252069 |
| ogbg-molmuv | mat_masking_200k  | forest       | ap       | 0.00252069 |
| ogbg-molmuv | mat_masking_20M   | forest       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-10M-MTR | linear       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-5M-MTR  | linear       | ap       | 0.00252069 |
| ogbg-molmuv | mat_masking_2M    | forest       | ap       | 0.00252069 |
| ogbg-molmuv | mat_masking_200k  | linear       | ap       | 0.00252069 |
| ogbg-molmuv | mol2vec           | forest       | ap       | 0.00252069 |
| ogbg-molmuv | ChemBERTa-5M-MTR  | forest       | ap       | 0.00252069 |

### ogbg-molsider (classification)

| dataset       | base_model        | head_model   | metric   |   result |
|:--------------|:------------------|:-------------|:---------|---------:|
| ogbg-molsider | rmat_4M           | linear       | rocauc   | 0.565157 |
| ogbg-molsider | rmat_4M_rdkit     | linear       | rocauc   | 0.548807 |
| ogbg-molsider | rmat_4M_rdkit     | forest       | rocauc   | 0.543047 |
| ogbg-molsider | mat_masking_2M    | linear       | rocauc   | 0.540698 |
| ogbg-molsider | mol2vec           | linear       | rocauc   | 0.539678 |
| ogbg-molsider | mat_masking_20M   | forest       | rocauc   | 0.539425 |
| ogbg-molsider | mat_masking_2M    | forest       | rocauc   | 0.539263 |
| ogbg-molsider | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.538553 |
| ogbg-molsider | ChemBERTa-77M-MTR | linear       | rocauc   | 0.536537 |
| ogbg-molsider | rmat_4M           | forest       | rocauc   | 0.535731 |
| ogbg-molsider | mat_masking_20M   | linear       | rocauc   | 0.533032 |
| ogbg-molsider | mat_masking_200k  | forest       | rocauc   | 0.531566 |
| ogbg-molsider | mol2vec           | forest       | rocauc   | 0.527451 |
| ogbg-molsider | mat_masking_200k  | linear       | rocauc   | 0.527033 |
| ogbg-molsider | ChemBERTa-77M-MTR | forest       | rocauc   | 0.526663 |
| ogbg-molsider | grover_base       | linear       | rocauc   | 0.525398 |
| ogbg-molsider | ChemBERTa-10M-MTR | linear       | rocauc   | 0.52021  |
| ogbg-molsider | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.519206 |
| ogbg-molsider | grover_large      | linear       | rocauc   | 0.51919  |
| ogbg-molsider | ChemBERTa-10M-MTR | forest       | rocauc   | 0.515792 |
| ogbg-molsider | grover_base       | forest       | rocauc   | 0.503591 |
| ogbg-molsider | grover_large      | forest       | rocauc   | 0.503448 |

### ogbg-moltox21 (classification)

| dataset       | base_model        | head_model   | metric   |   result |
|:--------------|:------------------|:-------------|:---------|---------:|
| ogbg-moltox21 | rmat_4M           | linear       | rocauc   | 0.610967 |
| ogbg-moltox21 | rmat_4M_rdkit     | linear       | rocauc   | 0.605261 |
| ogbg-moltox21 | mol2vec           | linear       | rocauc   | 0.603861 |
| ogbg-moltox21 | ChemBERTa-10M-MTR | linear       | rocauc   | 0.591052 |
| ogbg-moltox21 | mat_masking_2M    | linear       | rocauc   | 0.588861 |
| ogbg-moltox21 | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.582479 |
| ogbg-moltox21 | ChemBERTa-77M-MTR | linear       | rocauc   | 0.579727 |
| ogbg-moltox21 | mat_masking_20M   | linear       | rocauc   | 0.568553 |
| ogbg-moltox21 | mat_masking_2M    | forest       | rocauc   | 0.567389 |
| ogbg-moltox21 | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.566163 |
| ogbg-moltox21 | ChemBERTa-77M-MTR | forest       | rocauc   | 0.559167 |
| ogbg-moltox21 | mat_masking_200k  | forest       | rocauc   | 0.558419 |
| ogbg-moltox21 | grover_large      | linear       | rocauc   | 0.555958 |
| ogbg-moltox21 | mat_masking_200k  | linear       | rocauc   | 0.555659 |
| ogbg-moltox21 | mat_masking_20M   | forest       | rocauc   | 0.553639 |
| ogbg-moltox21 | rmat_4M_rdkit     | forest       | rocauc   | 0.551576 |
| ogbg-moltox21 | ChemBERTa-10M-MTR | forest       | rocauc   | 0.551278 |
| ogbg-moltox21 | mol2vec           | forest       | rocauc   | 0.550443 |
| ogbg-moltox21 | grover_base       | linear       | rocauc   | 0.545108 |
| ogbg-moltox21 | rmat_4M           | forest       | rocauc   | 0.5447   |
| ogbg-moltox21 | grover_large      | forest       | rocauc   | 0.514355 |
| ogbg-moltox21 | grover_base       | forest       | rocauc   | 0.512665 |

### ogbg-moltoxcast (classification)

| dataset         | base_model        | head_model   | metric   |   result |
|:----------------|:------------------|:-------------|:---------|---------:|
| ogbg-moltoxcast | rmat_4M_rdkit     | linear       | rocauc   | 0.519499 |
| ogbg-moltoxcast | rmat_4M           | linear       | rocauc   | 0.516141 |
| ogbg-moltoxcast | mol2vec           | linear       | rocauc   | 0.510599 |
| ogbg-moltoxcast | ChemBERTa-10M-MTR | linear       | rocauc   | 0.506748 |
| ogbg-moltoxcast | mat_masking_20M   | forest       | rocauc   | 0.504932 |
| ogbg-moltoxcast | mat_masking_2M    | linear       | rocauc   | 0.504809 |
| ogbg-moltoxcast | mat_masking_200k  | forest       | rocauc   | 0.504493 |
| ogbg-moltoxcast | grover_large      | linear       | rocauc   | 0.504284 |
| ogbg-moltoxcast | ChemBERTa-77M-MTR | forest       | rocauc   | 0.504269 |
| ogbg-moltoxcast | ChemBERTa-5M-MTR  | linear       | rocauc   | 0.504098 |
| ogbg-moltoxcast | mol2vec           | forest       | rocauc   | 0.503902 |
| ogbg-moltoxcast | ChemBERTa-10M-MTR | forest       | rocauc   | 0.503783 |
| ogbg-moltoxcast | mat_masking_200k  | linear       | rocauc   | 0.503369 |
| ogbg-moltoxcast | mat_masking_2M    | forest       | rocauc   | 0.502981 |
| ogbg-moltoxcast | ChemBERTa-5M-MTR  | forest       | rocauc   | 0.502916 |
| ogbg-moltoxcast | mat_masking_20M   | linear       | rocauc   | 0.502762 |
| ogbg-moltoxcast | ChemBERTa-77M-MTR | linear       | rocauc   | 0.502633 |
| ogbg-moltoxcast | grover_base       | linear       | rocauc   | 0.501782 |

