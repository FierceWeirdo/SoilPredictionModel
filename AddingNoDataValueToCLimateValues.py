#This file is no longer needed as it was used to add no data values to a CSV with just the data points
#This is not a requirement because we are converting CSVs to raster in the final model training setup

import pandas as pd

# Read both CSV files
sheet1 = pd.read_csv('Altum_DEM_Asc2.csv')
sheet2 = pd.read_csv('Climate_Vars_2029_Except_No_Data.csv')

# Iterate through each row in sheet1
new_rows = []
for index, row in sheet1.iterrows():
    easting_index = 0  # Assuming Easting column is the first column
    northing_index = 1  # Assuming Northing column is the second column
    easting = row[easting_index]
    northing = row[northing_index]
    
    # Check if the pair exists in sheet2
    if not ((sheet2['Easting'] == easting) & (sheet2['Northing'] == northing)).any():
        # Find the index where the new row should be inserted
        index_to_insert = sheet2['Easting'].searchsorted(easting)
        
        # Create a new row with interpolated values
        new_row = [easting, northing]
        for column in sheet2.columns[2:]:
            new_row.append(-99999.0)
        
        # Insert the new row at the correct position
        sheet2 = pd.concat([sheet2.iloc[:index_to_insert], pd.DataFrame([new_row], columns=sheet2.columns), sheet2.iloc[index_to_insert:]]).reset_index(drop=True)

# Write the updated sheet2 to a new CSV file
sheet2.to_csv('Climate_Data_2029.csv', index=False)
