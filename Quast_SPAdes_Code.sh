INPUT_FILE="/Users/mayank/Downloads/3622_SPAdes_Assembly/3622_SPAdes_Assembly.fa" #Example with 3622_SPAdes
OUTPUT_DIR="/Users/mayank/Downloads/SPAdes_Quast_Results"

# Extract base name for naming zip file and subdirectory
BASE_NAME=$(basename "$INPUT_FILE" .fa)

# Create a specific subdirectory for this input file
TEMP_OUTPUT_DIR="$OUTPUT_DIR/${BASE_NAME}_Quast"
mkdir -p "$TEMP_OUTPUT_DIR"

# Run QUAST and save results in the subdirectory
python3 /Users/mayank/miniconda3/bin/quast.py -o "$TEMP_OUTPUT_DIR" "$INPUT_FILE" && \

# Change to the temporary output directory
cd "$TEMP_OUTPUT_DIR" && \

# Zip the contents of the QUAST output directory without the full path
zip -r "../${BASE_NAME}_Quast.zip" . && \

# Return to the original directory
cd - >/dev/null

# Optional: Clean up temporary subdirectory
rm -rf "$TEMP_OUTPUT_DIR"


#

#Use this
python3 /Users/mayank/miniconda3/bin/quast.py -o /Users/mayank/Downloads/SPAdes_Quast_Results /Users/mayank/Downloads/2721_SPAdes_Assembly/2721_SPAdes_Assembly.fa
