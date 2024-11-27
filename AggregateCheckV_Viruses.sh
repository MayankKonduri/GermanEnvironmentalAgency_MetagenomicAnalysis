#!/bin/bash
  
# Create the output directory
output_dir="ReadyForVirSorter_v2_CheckV"
mkdir -p "$output_dir"
    
# Specify the .zip file to process (replace with your actual file name)
zip_file="5221_CheckV_v1.zip"
    
# Check if the file exists
if [ -f "$zip_file" ]; then
  # Extract the folder name from the zip file
  folder_name=$(basename "$zip_file" .zip)
  
  # Unzip the file with the -o flag to overwrite without asking
  unzip -qo "$zip_file" -d "$folder_name"
  
  # Check if the viruses.fna file exists in the extracted folder
  if [ -f "$folder_name/viruses.fna" ]; then
    # Rename and move the file to the output directory
    new_file_name="${folder_name%%_*}_viruses.fna"
    mv "$folder_name/viruses.fna" "$output_dir/$new_file_name"
    echo "Processed: viruses.fna has been renamed and moved."
  else
    echo "Warning: viruses.fna not found in $folder_name"
  fi

  # Clean up the extracted folder
  rm -rf "$folder_name"
else
  echo "Error: File $zip_file not found."
fi

echo "Processing complete."
