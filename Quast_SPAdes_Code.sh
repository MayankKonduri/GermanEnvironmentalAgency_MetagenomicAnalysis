INPUT_FILE="/Users/mayank/Downloads/3622_SPAdes_Assembly/3622_SPAdes_Assembly.fa" #Example with 3622_SPAdes
OUTPUT_DIR="/Users/mayank/Downloads/SPAdes_Quast_Results"

BASE_NAME=$(basename "$INPUT_FILE" .fa)

TEMP_OUTPUT_DIR="$OUTPUT_DIR/${BASE_NAME}_Quast"
mkdir -p "$TEMP_OUTPUT_DIR"

python3 /Users/mayank/miniconda3/bin/quast.py -o "$TEMP_OUTPUT_DIR" "$INPUT_FILE" && \

cd "$TEMP_OUTPUT_DIR" && \

zip -r "../${BASE_NAME}_Quast.zip" . && \

cd - >/dev/null

rm -rf "$TEMP_OUTPUT_DIR"


python3 /Users/mayank/miniconda3/bin/quast.py -o /Users/mayank/Downloads/SPAdes_Quast_Results /Users/mayank/Downloads/2721_SPAdes_Assembly/2721_SPAdes_Assembly.fa
