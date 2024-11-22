import pandas as pd

# Define file paths
excel_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_Summary_VirSorter2_wTrimmed.xlsx'  # Excel file path
fasta_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_VirSorter2_Assembly/3622_VirSorter2_Assembly.fa'  # Your .fa file
output_fasta_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_VirSorter2_Assembly_Filtered.fa'  # Corrected path to save filtered sequences

# Step 1: Read the filtered Excel file and extract the 'seqname' column
excel_data = pd.read_excel(excel_file_path, sheet_name='Filtered')
filtered_seqnames = excel_data['seqname'].tolist()

# Step 2: Read the .fa (FASTA) file and filter sequences
def filter_fasta(fasta_file, seqnames_to_keep):
    with open(fasta_file, 'r') as f:
        filtered_sequences = []
        seq_header = None
        seq_data = []
        
        for line in f:
            line = line.strip()
            
            if line.startswith('>'):  # This is a header line
                # If we have a previous sequence, check if it should be kept
                if seq_header and seq_header[1:] in seqnames_to_keep:  # Match header without '>'
                    filtered_sequences.append(f"{seq_header}\n{''.join(seq_data)}")
                
                # Reset for new sequence
                seq_header = line
                seq_data = []
            else:
                seq_data.append(line)
        
        # Don't forget to handle the last sequence in the file
        if seq_header and seq_header[1:] in seqnames_to_keep:
            filtered_sequences.append(f"{seq_header}\n{''.join(seq_data)}")
        
    return filtered_sequences

# Filter the FASTA sequences
filtered_fasta = filter_fasta(fasta_file_path, filtered_seqnames)

# Step 3: Write the filtered sequences to a new FASTA file
with open(output_fasta_path, 'w') as output_fasta:
    output_fasta.write("\n".join(filtered_fasta))

print(f"Filtered sequences have been saved to {output_fasta_path}")
