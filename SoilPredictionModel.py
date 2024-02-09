import rasterio
from rasterio.plot import show
from rasterio.transform import rowcol
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Step 1: Load TIFF files
def load_tiff(file_path):
    with rasterio.open(file_path) as src:
        # Read the raster data
        raster_data = src.read()
        # Extract metadata
        metadata = src.meta
        # Extract transform function
        transform = src.transform
    return raster_data, metadata, transform

# Example usage
file_path_drone1 = 'SoilPredictionModel/terrain_rasters/Altum/Altum_Aspect.tif'
file_path_drone2 = 'SoilPredictionModel/terrain_rasters/Altum/Altum_Convergence.tif'

raster_data_drone1, metadata_drone1, transform_drone1 = load_tiff(file_path_drone1)
raster_data_drone2, metadata_drone2, transform_drone2 = load_tiff(file_path_drone2)

# Step 2: Load CSV file
ground_truth_data = pd.read_csv("SoilPredictionModel/fieldSurveyData.csv")

# Function to convert geographic coordinates to pixel coordinates
def lat_lon_to_pixel(lat, lon, transform):
    col, row = rowcol(transform, lon, lat)
    return row, col

# Step 3: Merge raster data with ground truth
for index, row in ground_truth_data.iterrows():
    lat, lon = row['LAT'], row['LNG']
    ground_truth_value = row['BARE_GROUND']
    
    # Convert geographic coordinates to pixel coordinates for drone 1
    row_drone1, col_drone1 = lat_lon_to_pixel(lat, lon, transform_drone1)
    # Convert geographic coordinates to pixel coordinates for drone 2
    row_drone2, col_drone2 = lat_lon_to_pixel(lat, lon, transform_drone2)

    # Check if pixel coordinates are within the raster bounds
    if (0 <= row_drone1 < raster_data_drone1.shape[1]) and (0 <= col_drone1 < raster_data_drone1.shape[2]):
        # Associate ground truth value with pixel in raster data for drone 1
        ground_truth_data.at[index, 'raster1_value'] = raster_data_drone1[:, row_drone1, col_drone1]
    else:
        # Skip this pixel if ground truth is not available
        ground_truth_data.at[index, 'raster1_value'] = np.nan
    
    if (0 <= row_drone2 < raster_data_drone2.shape[1]) and (0 <= col_drone2 < raster_data_drone2.shape[2]):
        # Associate ground truth value with pixel in raster data for drone 2
        ground_truth_data.at[index, 'raster2_value'] = raster_data_drone2[:, row_drone2, col_drone2]
    else:
        # Skip this pixel if ground truth is not available
        ground_truth_data.at[index, 'raster2_value'] = np.nan


# Example usage to visualize the merged data for drone 1
plt.figure(figsize=(10, 6))

# Plot raster data
plt.imshow(raster_data_drone1[:, :, 0], cmap='gray')

# Plot ground truth values as markers
plt.scatter(row_drone1, col_drone1, color='red', marker='x', label='Ground Truth')

plt.xlabel('Pixel Column')
plt.ylabel('Pixel Row')
plt.title('Visualization of Merged Data for Drone 1')
plt.legend()
plt.show()


# Now ground_truth_data DataFrame contains ground truth values along with corresponding raster values

# Step 4: Spatial cross-validation (implement k-fold spatial cross-validation)

# Step 5: Prepare data for training
# Extract features from TIFF files and ground truth values

# Step 6: Train a Random Forest model
X_train, X_test, y_train, y_test = train_test_split(features, ground_truth_values, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: Evaluate the model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)
