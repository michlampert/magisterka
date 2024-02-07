#!/bin/bash
#SBATCH --time=8:00:00
#SBATCH --mem=32G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -C memfs
#SBATCH --partition=plgrid
#SBATCH -o logs.txt
#SBATCH --array=0-247

ml gcc/11.3.0
ml python/3.10.4-gcccore-11.3.0

source ./venv/bin/activate

python embedding_procedure.py \
    --id $SLURM_ARRAY_TASK_ID

