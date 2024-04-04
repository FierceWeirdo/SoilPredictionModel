import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from GetInputFiles import get_paths_to_files, load_tiff
from GetFeaturesAndGroundTruth import get_all_raster_values_for_ground_truth, get_all_bare_ground_values_as_array

#The training of the model takes place here

altum_terrain_paths = get_paths_to_files('altum_terrain')
climate_2034 = get_paths_to_files('climate_2034')

paths_array = np.concatenate((altum_terrain_paths, climate_2034))
feature_values_array = get_all_raster_values_for_ground_truth(paths_array)
bare_ground_values = get_all_bare_ground_values_as_array()

feature_df = pd.DataFrame(feature_values_array)

# Replace NaN values 
feature_df.fillna(-99999.0, inplace=True)

feature_values_array = feature_df.values

print("Feature Values Array Shape:", feature_values_array.shape)
print("Bare Ground Values Shape:", bare_ground_values.shape)

# Initialize the RandomForestRegressor 
rf_regressor = RandomForestRegressor(
    n_estimators = 500,
    max_depth = None,
    min_samples_split = 8,
    min_samples_leaf = 4,
    random_state=45
)

# Kfold initialisation
num_folds = 5
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

# Perform K-fold cross-validation
mae_scores = []

for train_index, test_index in kf.split(feature_values_array):
    X_train, X_test = feature_values_array[train_index], feature_values_array[test_index]
    y_train, y_test = bare_ground_values[train_index], bare_ground_values[test_index]
    
    # Train the model
    rf_regressor.fit(X_train, y_train)
    
    # Predict
    y_pred = rf_regressor.predict(X_test)
    
    # Calculate mean absolute error and append to the list
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores.append(mae)

# Taking mean of the mean absolute errors
mean_mae = np.mean(mae_scores)
print("Mean Absolute Error:", mean_mae)

# Save trained model
model_file_path = 'trained_rf_model_future_2034.joblib'
joblib.dump(rf_regressor, model_file_path)
print(f"Trained model saved to {model_file_path}")
