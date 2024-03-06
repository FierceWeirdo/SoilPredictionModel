import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import KFold
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from GetInputFiles import get_paths_to_files, load_tiff
from GetFeaturesAndGroundTruth import get_all_raster_values_for_ground_truth, get_all_bare_ground_values_as_array

# Load data
altum_terrain_paths = get_paths_to_files('altum_terrain')
altum_climate_paths = get_paths_to_files('climate_altum')
altum_ndvi_savi_paths = get_paths_to_files('altum_ndvi_savi')

paths_array = np.concatenate((altum_terrain_paths, altum_climate_paths, altum_ndvi_savi_paths))
feature_values_array = get_all_raster_values_for_ground_truth(paths_array)
bare_ground_values = get_all_bare_ground_values_as_array()

feature_df = pd.DataFrame(feature_values_array)

# Fill NaN values with the mean of each feature
feature_df.fillna(feature_df.mean(), inplace=True)

# Convert back to numpy array
feature_values_array = feature_df.values

print("Feature Values Array Shape:", feature_values_array.shape)
print("Bare Ground Values Shape:", bare_ground_values.shape)

# Initialize RandomForestRegressor
rf_regressor = RandomForestRegressor(
    n_estimators = 1000,
    max_depth = 15,
    min_samples_split = 6,
    min_samples_leaf = 3,
    random_state=44
)

# Initialize KFold
num_folds = 5
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

# Perform K-fold cross-validation with selected features
mae_scores_selected_features = []

for train_index, test_index in kf.split(feature_values_array):
    X_train_selected, X_test_selected = feature_values_array[train_index], feature_values_array[test_index]
    y_train, y_test = bare_ground_values[train_index], bare_ground_values[test_index]
    
    # Initialize and fit the RandomForestRegressor
    rf_regressor.fit(X_train_selected, y_train)

    # Predict on the test set
    y_pred = rf_regressor.predict(X_test_selected)
    
    # Calculate mean absolute error and append to the list
    mae = mean_absolute_error(y_test, y_pred)
    print('Prediction: ')
    print(y_pred)
    print('Truth: ')
    print(y_test)
    mae_scores_selected_features.append(mae)

# Calculate the mean of the mean absolute errors
mean_mae_selected_features = np.mean(mae_scores_selected_features)
print("Mean Absolute Error with selected features:", mean_mae_selected_features)

model_file_path = 'trained_rf_model_with_all_features.joblib'
joblib.dump(rf_regressor, model_file_path)
print(f"Trained model saved to {model_file_path}")