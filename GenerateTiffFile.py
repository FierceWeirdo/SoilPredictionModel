import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from GetInputFiles import get_paths_to_files, load_tiff
import joblib
import rasterio

altum_terrain_paths = get_paths_to_files('altum_terrain')
# altum_climate_paths = get_paths_to_files('climate_altum')
altum_ndvi_savi_paths = get_paths_to_files('altum_ndvi_savi')
climate_2029 = get_paths_to_files('climate_2029')

paths_array = np.concatenate((altum_terrain_paths, altum_ndvi_savi_paths, climate_2029))

feature_values_list = []

for file in paths_array:
    with rasterio.open(file) as src:
        raster_data = src.read(1, window=((1000, 2000), (17500, 18552)))
        feature_values_list.append(raster_data)

# Stacking all the feauteres from raster files
feature_values_array = np.stack(feature_values_list, axis=-1)

num_pixels = feature_values_array.shape[0] * feature_values_array.shape[1]
feature_values_array_2d = feature_values_array.reshape(num_pixels, feature_values_array.shape[2])

#loading the trained model
rf_model = joblib.load('trained_rf_model_future_2029.joblib')

# Predicting the probability
predicted_probabilities = rf_model.predict(feature_values_array_2d) / 100
print(predicted_probabilities)

# Change raster shape to original
predicted_probabilities_raster = predicted_probabilities.reshape(feature_values_array.shape[0], feature_values_array.shape[1])

# Save and write probabilities to a GeoTIFF File
output_file = 'future_2029_first_half.tif'

with rasterio.open(paths_array[0]) as src:  
    profile = src.profile
    profile.update(
        dtype=rasterio.float32,
        count=1,
        compress='lzw',
        width=1000,
        height=1000,
        nodata=1.818800511597591651e-01, 
    )
    with rasterio.open(output_file, 'w', **profile) as dst:
        dst.write(predicted_probabilities_raster.astype(rasterio.float32), 1)

print("Raster file created successfully.")
