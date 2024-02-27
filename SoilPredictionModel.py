import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from GetInputFiles import get_paths_to_files
from GetFeaturesAndGroundTruth import get_all_raster_values_for_ground_truth, get_all_bare_ground_values_as_array

# Load data
altum_terrain_paths = get_paths_to_files('altum_terrain')
altum_climate_paths = get_paths_to_files('climate_altum')
paths_array = np.concatenate((altum_terrain_paths, altum_climate_paths))
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
    n_estimators=1500,
    max_depth=None,
    min_samples_split=20,
    min_samples_leaf=8
)

# Initialize KFold
num_folds = 7
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

# Initialize RFECV
rfecv = RFECV(estimator=rf_regressor, cv=kf)

# Fit RFECV
rfecv.fit(feature_values_array, bare_ground_values)

# Get selected features
selected_feature_values_array = feature_values_array[:, rfecv.support_]

# Perform K-fold cross-validation with selected features
mae_scores_selected_features = []

for train_index, test_index in kf.split(selected_feature_values_array):
    X_train_selected, X_test_selected = selected_feature_values_array[train_index], selected_feature_values_array[test_index]
    y_train, y_test = bare_ground_values[train_index], bare_ground_values[test_index]
    
    # Initialize and fit the RandomForestRegressor
    rf_regressor.fit(X_train_selected, y_train)

    # Predict on the test set
    y_pred = rf_regressor.predict(X_test_selected)
    
    # Calculate mean absolute error and append to the list
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores_selected_features.append(mae)

# Calculate the mean of the mean absolute errors
mean_mae_selected_features = np.mean(mae_scores_selected_features)
print("Mean Absolute Error with selected features:", mean_mae_selected_features)
