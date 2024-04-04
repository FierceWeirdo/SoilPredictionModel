#This file was written when we were trying to run ClimateBC for all 192 million points
#No longer needed but can be used in case the file needs to be appended together

import pandas as pd

# Read the first CSV file
csv1 = pd.read_csv('Altum_DEM_CSV_All_Rows_13GCMs_ensemble_ssp126_2029Y.csv')

# Read the second CSV file, skipping the header row
csv2 = pd.read_csv('Altum_DEM_CSV_Remaining_Rows_13GCMs_ensemble_ssp126_2029Y.csv.csv')

# Append the two CSV files
result = pd.concat([csv1, csv2], ignore_index=True)

# Write the result to a new CSV file
result.to_csv('Climate_Vars_2029.csv', index=False)
