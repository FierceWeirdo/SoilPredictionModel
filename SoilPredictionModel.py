import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import KFold
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from GetInputFiles import get_paths_to_files, load_tiff
from GetFeaturesAndGroundTruth import get_all_raster_values_for_ground_truth, get_all_bare_ground_values_as_array

#The training of the current soil prediction model takes place here

altum_terrain_paths = get_paths_to_files('altum_terrain')
altum_climate_paths = get_paths_to_files('climate_altum')
altum_ndvi_savi_paths = get_paths_to_files('altum_ndvi_savi')

paths_array = np.concatenate((altum_terrain_paths, altum_climate_paths, altum_ndvi_savi_paths))
feature_values_array = get_all_raster_values_for_ground_truth(paths_array)
bare_ground_values = get_all_bare_ground_values_as_array()

feature_df = pd.DataFrame(feature_values_array)

# Replace NaN values 
feature_df.fillna(-99999.0, inplace=True)

feature_values_array = feature_df.values

print("Feature Values Array Shape:", feature_values_array.shape)
print("Bare Ground Values Shape:", bare_ground_values.shape)

# Initialize the RandomForestRegressor 
# Params:    n_estimators = 500,
            # max_depth = None,
            # min_samples_split = 8,
            # min_samples_leaf = 4,
            # random_state=45
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

# Initialize Random Forest Recursive Feature elimination (RFECV)
rfecv = RFECV(estimator=rf_regressor, cv=kf)

# Perform K-fold cross-validation with recursive feature elimination
mae_scores_selected_features = []

for train_index, test_index in kf.split(feature_values_array):
    X_train_selected, X_test_selected = feature_values_array[train_index], feature_values_array[test_index]
    y_train, y_test = bare_ground_values[train_index], bare_ground_values[test_index]
    
    # Get selected features and their values
    rfecv.fit(X_train_selected, y_train)
    selected_features_mask = rfecv.support_
    feature_names = feature_df.columns
    selected_features = feature_names[selected_features_mask]
    print("Selected Features:", selected_features)

    rf_regressor.fit(X_train_selected[:, selected_features_mask], y_train) # Train on set
    
    y_pred = rf_regressor.predict(X_test_selected[:, selected_features_mask]) #Prediction on set
    
    # Calculate mean absolute error and append to the list
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores_selected_features.append(mae)

# Taking mean of the mean absolute errors
mean_mae_selected_features = np.mean(mae_scores_selected_features)
print("Mean Absolute Error with selected features:", mean_mae_selected_features)

# Save trained model
model_file_path = 'trained_rf_model_with_selected_features.joblib'
joblib.dump(rf_regressor, model_file_path)
print(f"Trained model saved to {model_file_path}")
