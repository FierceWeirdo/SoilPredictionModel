import rasterio
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from GetInputFiles import get_paths_to_files, load_tiff
import joblib

# Load data
altum_terrain_paths = get_paths_to_files('altum_terrain')
altum_climate_paths = get_paths_to_files('climate_altum')
altum_ndvi_savi_paths = get_paths_to_files('altum_ndvi_savi')

# Concatenate all paths
paths_array = np.concatenate((altum_terrain_paths, altum_climate_paths, altum_ndvi_savi_paths))

# Initialize an empty list to store features
feature_values_list = []

for file in paths_array:
    with rasterio.open(file) as src:
        raster_data = src.read(1, window=((5351, 10351), (0, 18552)))
        feature_values_list.append(raster_data)

# src.profile = {'driver': 'GTiff', 'dtype': 'float32', 'nodata': -99999.0, 'width': 18552, 'height': 10351, 'count': 1, 'crs': CRS.from_epsg(3005), 'transform': Affine(0.5, 0.0, 1358941.0,
# 0.0, -0.5, 656280.0), 'blockysize': 1, 'tiled': False, 'compress': 'lzw', 'interleave': 'band'}

# Stack the features
feature_values_array = np.stack(feature_values_list, axis=-1)

# Reshape the data to match the input requirements of your model
num_pixels = feature_values_array.shape[0] * feature_values_array.shape[1]
feature_values_array_2d = feature_values_array.reshape(num_pixels, feature_values_array.shape[2])

# Load the trained machine learning model
rf_model = joblib.load('SoilPredictionModel/trained_rf_model_with_all_features.joblib')

# Use the model to predict the probability of soil for each pixel
predicted_probabilities = rf_model.predict(feature_values_array_2d) / 100
print(predicted_probabilities)

np.savetxt("some_i.txt", predicted_probabilities ,delimiter=',')
# Reshape the predicted probabilities back to the original raster shape
predicted_probabilities_raster = predicted_probabilities.reshape(feature_values_array.shape[0], feature_values_array.shape[1])

# Save the predicted probabilities as a GeoTIFF file
output_file = 'predicted_soil_probability_12.tif'

# Write the predicted probabilities to a new GeoTIFF file
with rasterio.open(paths_array[0]) as src:  
    profile = src.profile
    profile.update(
        dtype=rasterio.float32,
        count=1,
        compress='lzw',
        width=18552,
        height=5000,
        nodata=1.818800511597591651e-01, 
    )
    with rasterio.open(output_file, 'w', **profile) as dst:
        dst.write(predicted_probabilities_raster.astype(rasterio.float32), 1)

print("Predicted soil probability GeoTIFF file saved successfully.")
