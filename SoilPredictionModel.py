import rasterio
from rasterio.plot import show
from rasterio.transform import rowcol
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from GetInputFiles import get_paths_to_files
from GetFeaturesAndGroundTruth import get_all_raster_values_for_ground_truth, get_all_bare_ground_values_as_array

altum_terrain_paths = get_paths_to_files('m3m_terrain')
feature_values_array = get_all_raster_values_for_ground_truth(altum_terrain_paths)
bare_ground_values = get_all_bare_ground_values_as_array()

print("Feature Values Array Shape:", feature_values_array.shape)
print("Bare Ground Values Shape:", bare_ground_values.shape)
num_folds = 5
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

mae_scores = []
for train_index, test_index in kf.split(feature_values_array):
    X_train, X_test = feature_values_array[train_index], feature_values_array[test_index]
    y_train, y_test = bare_ground_values[train_index], bare_ground_values[test_index]
    
    # Initialize and fit the RandomForestRegressor
    rf_regressor = RandomForestRegressor(
        n_estimators=100,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1
    )
    rf_regressor.fit(X_train, y_train)

    # Predict on the test set
    y_pred = rf_regressor.predict(X_test)
    print('Predictions:')
    print(y_pred)
    print('Truth:')
    print(y_test)

    # Calculate mean absolute error and append to the list
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores.append(mae)

# Calculate the mean of the mean absolute errors
mean_mae = np.mean(mae_scores)
print(Y_pred)
print("Mean Absolute Error:", mean_mae)
