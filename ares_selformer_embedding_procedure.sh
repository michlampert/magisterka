#!/bin/bash
#SBATCH --time=3:00:00
#SBATCH --mem=5G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -C memfs
#SBATCH --partition=plgrid
#SBATCH -o logs.txt
#SBATCH --array=1-93

line=$(sed -n "${SLURM_ARRAY_TASK_ID}p" selformer_params.txt)

IFS=" " read -r dataset_name <<< "$line"

ml gcc/11.3.0
ml python/3.10.4-gcccore-11.3.0

source ./venv/bin/activate

python SELFormer/produce_embeddings.py --selfies_dataset=selfies/$dataset_name.csv --model_file=models/modelO --embed_file=selformer_embeddings/$dataset_name.csv
