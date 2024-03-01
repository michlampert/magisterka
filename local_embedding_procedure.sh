source ./venv/bin/activate

for id in {1..1}; do
    line=$(sed -n "${id}p" embedding_params.txt)

    IFS=" " read -r dataset_name model_name <<< "$line"

    echo "python3 embedding_procedure.py --model_name $model_name --dataset_name $dataset_name --max_samples 10"

    python3 embedding_procedure.py --model_name $model_name --dataset_name $dataset_name --max_samples 10
done