import pandas as pd

excel_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_Summary_VirSorter2_wTrimmed.xlsx'
fasta_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_VirSorter2_Assembly/3622_VirSorter2_Assembly.fa'
output_fasta_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_VirSorter2_Assembly_Filtered.fa'

excel_data = pd.read_excel(excel_file_path, sheet_name='Filtered')
filtered_seqnames = excel_data['seqname'].tolist()

def filter_fasta(fasta_file, seqnames_to_keep):
    with open(fasta_file, 'r') as f:
        filtered_sequences = []
        seq_header = None
        seq_data = []
        
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq_header and seq_header[1:] in seqnames_to_keep:
                    filtered_sequences.append(f"{seq_header}\n{''.join(seq_data)}")
                seq_header = line
                seq_data = []
            else:
                seq_data.append(line)
        
        if seq_header and seq_header[1:] in seqnames_to_keep:
            filtered_sequences.append(f"{seq_header}\n{''.join(seq_data)}")
        
    return filtered_sequences

filtered_fasta = filter_fasta(fasta_file_path, filtered_seqnames)

with open(output_fasta_path, 'w') as output_fasta:
    output_fasta.write("\n".join(filtered_fasta))

print(f"Filtered sequences have been saved to {output_fasta_path}")
