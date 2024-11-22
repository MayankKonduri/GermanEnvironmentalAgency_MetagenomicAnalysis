import pandas as pd

# Define the input and output file paths
input_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_Summary_VirSorter2.xlsx'  # Input file
output_file_path = '/Users/mayank/Downloads/3622_VirSorter2/3622_Summary_VirSorter2_wTrimmed.xlsx'  # Output file

# Load the .xlsx file, skipping the first row
data = pd.read_excel(input_file_path, skiprows=1)

# Ensure numeric columns are properly interpreted
data['max_score'] = pd.to_numeric(data['max_score'], errors='coerce')
data['length'] = pd.to_numeric(data['length'], errors='coerce')

# Filter rows where max_score >= 0.5 and length >= 1500
filtered_data = data[(data['max_score'] >= 0.5) & (data['length'] >= 1500)]

# Write the original data and the filtered data to separate sheets in the same Excel file
with pd.ExcelWriter(output_file_path, mode='w', engine='openpyxl') as writer:
    data.to_excel(writer, sheet_name='Original', index=False)  # Original data in 'Original' sheet
    filtered_data.to_excel(writer, sheet_name='Filtered', index=False)  # Filtered data in 'Filtered' sheet

print(f"Original and filtered data have been saved to separate sheets in {output_file_path}")
