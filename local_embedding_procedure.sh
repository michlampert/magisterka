source ./venv/bin/activate

for id in {7..7}; do
    python3 embedding_procedure.py --id $id --max_samples 10
done