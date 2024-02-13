import rasterio
from rasterio.plot import show
from rasterio.transform import rowcol
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from GetInputFiles import get_altum_terrain_rasters 
from GetCSVDataAsArray import get_ground_truth_array

def load_tiff(file_path):
    with rasterio.open(file_path) as src:
        # Read the raster data
        raster_data = src.read()
        # Extract metadata
        metadata = src.meta
        # Extract transform function
        transform = src.transform
        # Extract transform function
        raster_sample = src.sample
    return raster_data, metadata, transform, raster_sample

# Step 1: Load TIFF files
raster_data, metadata, transform, raster_sample = load_tiff('SoilPredictionModel/terrain_rasters/Altum/Altum_DAH.tif')
print(metadata)
# altum_aspect_data = altum_raster_data['altum_aspect_data']
# altum_aspect_transform = altum_raster_data['altum_aspect_transform']
# altum_aspect_metadata = altum_raster_data['altum_aspect_metadata']
# width = altum_aspect_metadata['width']
# height = altum_aspect_metadata['height']

# Initialize an empty list to store the coordinates
# coordinates = []
# print(raster_data[0][0][1])
# #Loop through each pixel and transform its coordinates to BC Albers CRS
# for y in range(min(100, metadata['height'])):
#     for x in range(min(100, metadata['width'])):
#         # Transform pixel coordinates to BC Albers CRS
#         x_bc_albers, y_bc_albers = transform * (x, y)   
#         pixel_value = raster_data[0][y][x]
#         coordinates.append([x_bc_albers, y_bc_albers, pixel_value])

# # Now 'coordinates' contains a list of [x_bc_albers, y_bc_albers] pairs for each pixel in the raster
# print('Coordinates:')
# print(coordinates)
# print(len(coordinates))

# Step 2: Load CSV file
ground_truth_data = get_ground_truth_array()
#print(ground_truth_data)


# ground_truth_data now stores [[northing, easting, altitude, bare_ground], ...] for 239 pixels

# # Step 3: Get 

# # Now ground_truth_data DataFrame contains ground truth values along with corresponding raster values

# # Step 4: Spatial cross-validation (implement k-fold spatial cross-validation)

# # Step 5: Prepare data for training
# # Extract features from TIFF files and ground truth values

# # Step 6: Train a Random Forest model
# X_train, X_test, y_train, y_test = train_test_split(features, ground_truth_values, test_size=0.2, random_state=42)
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Step 7: Evaluate the model
# predictions = model.predict(X_test)
# mae = mean_absolute_error(y_test, predictions)
# print("Mean Absolute Error:", mae)
