#!/bin/bash
  
output_dir="ReadyForVirSorter_v2_CheckV"
mkdir -p "$output_dir"
    
zip_file="5221_CheckV_v1.zip"
    
if [ -f "$zip_file" ]; then
  folder_name=$(basename "$zip_file" .zip)
  
  unzip -qo "$zip_file" -d "$folder_name"
  
  if [ -f "$folder_name/viruses.fna" ]; then
    new_file_name="${folder_name%%_*}_viruses.fna"
    mv "$folder_name/viruses.fna" "$output_dir/$new_file_name"
    echo "Processed: viruses.fna has been renamed and moved."
  else
    echo "Warning: viruses.fna not found in $folder_name"
  fi

  rm -rf "$folder_name"
else
  echo "Error: File $zip_file not found."
fi

echo "Processing complete."
