import pandas as pd
import numpy as np
import pyproj

df = pd.read_csv('Altum_DEM_ASC2.csv', header=None)

# Generate random unique IDs for ID1 and ID2
df['ID1'] = np.random.randint(1000000, 9999999, size=len(df))
df['ID2'] = np.random.randint(1000000, 9999999, size=len(df))

# Assign column names
df.columns = ['easting', 'northing', 'elevation', 'ID1', 'ID2']

# Define the projection transformation from EPSG:3005 to EPSG:4326 (WGS84 - Lat/Lng)
bc_albers = pyproj.Proj(init='epsg:3005')
wgs84 = pyproj.Proj(init='epsg:4326')

# Convert easting, northing to latitude, longitude
df['Long'], df['Lat'] = pyproj.transform(bc_albers, wgs84, df['easting'].values, df['northing'].values)

# Rename elevation column to 'Elev'
df.rename(columns={'elevation': 'Elev'}, inplace=True)

# Remove rows where elevation is -99999
df = df[df['Elev'] != -99999]

# Reorder columns
df = df[['ID1', 'ID2', 'Lat', 'Long', 'Elev']]

# Write to a new CSV file
df.to_csv('Altum_DEM_CSV_Final.csv', index=False)
