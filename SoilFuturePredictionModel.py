import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import KFold
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from GetInputFiles import get_paths_to_files, load_tiff
from GetFeaturesAndGroundTruth import get_all_raster_values_for_ground_truth_including_climate, get_all_bare_ground_values_as_array

# Load data from CSV file
csv_file_path = 'Climate_Vars_2029_Except_No_Data.csv'

# Load remaining features from raster files as before
altum_terrain_paths = get_paths_to_files('altum_terrain')
altum_climate_paths = get_paths_to_files('climate_altum')

paths_array = np.concatenate((altum_terrain_paths, altum_climate_paths))
raster_feature_values = get_all_raster_values_for_ground_truth_including_climate(paths_array, csv_file_path)

# Combine raster features with climate variables
feature_values_array = np.concatenate((raster_feature_values, climate_variables), axis=1)

feature_df = pd.DataFrame(feature_values_array)

# Fill NaN values with the mean of each feature
feature_df.fillna(-99999.0, inplace=True)

# Convert back to numpy array
feature_values_array = feature_df.values

print("Feature Values Array Shape:", feature_values_array.shape)
print("Bare Ground Values Shape:", bare_ground_values.shape)

# Initialize RandomForestRegressor
rf_regressor = RandomForestRegressor(
    n_estimators = 500,
    max_depth = None,
    min_samples_split = 8,
    min_samples_leaf = 4,
    random_state=45
)

# Initialize KFold
num_folds = 5
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

# Initialize RFECV
rfecv = RFECV(estimator=rf_regressor, cv=kf)

# Perform K-fold cross-validation with recursive feature elimination
mae_scores_selected_features = []

for train_index, test_index in kf.split(feature_values_array):
    X_train_selected, X_test_selected = feature_values_array[train_index], feature_values_array[test_index]
    y_train, y_test = bare_ground_values[train_index], bare_ground_values[test_index]
    
    # Fit RFECV on training data
    rfecv.fit(X_train_selected, y_train)

    # Get the boolean array indicating selected features
    selected_features_mask = rfecv.support_

    # Get the names of the features
    feature_names = feature_df.columns

    # Get the selected features
    selected_features = feature_names[selected_features_mask]

    print("Selected Features:", selected_features)

    # Train using only selected features
    rf_regressor.fit(X_train_selected[:, selected_features_mask], y_train)

    # Predict on the test set
    y_pred = rf_regressor.predict(X_test_selected[:, selected_features_mask])
    
    # Calculate mean absolute error and append to the list
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores_selected_features.append(mae)

# Calculate the mean of the mean absolute errors
mean_mae_selected_features = np.mean(mae_scores_selected_features)
print("Mean Absolute Error with selected features:", mean_mae_selected_features)

# Save trained model
model_file_path = 'trained_future_rf_model_with_selected_features.joblib'
joblib.dump(rf_regressor, model_file_path)
print(f"Trained model saved to {model_file_path}")
