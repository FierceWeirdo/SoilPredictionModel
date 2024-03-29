import pandas as pd

##tested this code with 2 small CSVs - it works
# Read the first CSV file
csv1 = pd.read_csv('Altum_DEM_CSV_All_Rows_13GCMs_ensemble_ssp126_2029Y.csv')
# csv1 = pd.read_csv('test1.csv')

# Read the second CSV file, skipping the header row
csv2 = pd.read_csv('Altum_DEM_CSV_Remaining_Rows_13GCMs_ensemble_ssp126_2029Y.csv.csv')
# csv2 = pd.read_csv('test2.csv')

# Append the two CSV files
result = pd.concat([csv1, csv2], ignore_index=True)

# Write the result to a new CSV file
result.to_csv('Climate_Vars_2029.csv', index=False)
