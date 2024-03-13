#!/bin/bash
#SBATCH --time=0:08:00
#SBATCH --mem=6G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -C memfs
#SBATCH --partition=plgrid
#SBATCH -o logs_predict.txt
#SBATCH -A plgbit2-cpu
#SBATCH --array=1-341

line=$(sed -n "${SLURM_ARRAY_TASK_ID}p" predict_params.txt)

IFS=" " read -r dataset_name base_model head_model <<< "$line"

ml gcc/11.3.0
ml python/3.10.4-gcccore-11.3.0

source ./venv/bin/activate

python predict_procedure.py \
    --dataset_name $dataset_name \
    --base_model $base_model \
    --head_model $head_model
