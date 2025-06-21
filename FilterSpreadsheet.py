import pandas as pd

input_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_Summary_VirSorter2.xlsx' 
output_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_Summary_VirSorter2_wTrimmed.xlsx' 

data = pd.read_excel(input_file_path, skiprows=1)

data['max_score'] = pd.to_numeric(data['max_score'], errors='coerce')
data['length'] = pd.to_numeric(data['length'], errors='coerce')

filtered_data = data[(data['max_score'] >= 0.5) & (data['length'] >= 1500)]

with pd.ExcelWriter(output_file_path, mode='w', engine='openpyxl') as writer:
    data.to_excel(writer, sheet_name='Original', index=False)
    filtered_data.to_excel(writer, sheet_name='Filtered', index=False)  

print(f"Original and filtered data have been saved to separate sheets in {output_file_path}")
