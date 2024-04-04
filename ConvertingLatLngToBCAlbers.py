import pandas as pd
import numpy as np
import pyproj

#After getting data from ClimateBC, use this file to convert the Lat Long to BC Albers to match with all existing data

# Read the CSV file
df = pd.read_csv('Altum_DEM_CSV_Final_13GCMs_ensemble_ssp126_2034Y.csv')
print('Done reading CSV.')

# Define the projection transformation from EPSG:4326 (WGS84 - Lat/Lng) to EPSG:3005 (BC Albers)
wgs84 = pyproj.Proj(init='epsg:4326')
bc_albers = pyproj.Proj(init='epsg:3005')

# Convert latitude and longitude to BC Albers projection
x, y = pyproj.transform(wgs84, bc_albers, df['Longitude'].values, df['Latitude'].values)
print('Done transforming CSV.')
# Round the coordinates to 2 decimal points
x = np.round(x, decimals=2)
y = np.round(y, decimals=2)

# Update the DataFrame with the rounded coordinates
df['Easting'] = x
df['Northing'] = y
print('Done updating Easting Northing Values in CSV.')
df.drop(columns=['Latitude', 'Longitude', 'Elevation'], inplace=True)

# Reorder columns putting Easting and Northing first
cols = df.columns.tolist()
cols = ['Easting', 'Northing'] + [col for col in cols if col not in ['Easting', 'Northing', 'ID1', 'ID2']]
df = df[cols]

# Write the updated DataFrame to a new CSV file
df.to_csv('Climate_Vars_2034.csv', index=False)
print('Done creating new CSV.')
