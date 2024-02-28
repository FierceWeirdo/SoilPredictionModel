# Bare Ground Prediction Model with Random Forest and Recursive Feature Elimination

## Overview

This project involves building a machine learning model to predict the percentage of bare ground over a certain set of land based on terrain files. The model uses the Random Forest algorithm, known for its robustness and versatility in handling regression tasks. Additionally, Recursive Feature Elimination (RFE) is employed for feature selection to enhance the model's performance.

## Usage

1. **Dependencies**: Make sure you have the following dependencies installed:
   - `numpy`
   - `pandas`
   - `scikit-learn`
   - `joblib`
   - `rasterio`

2. **Installation**: Clone this repository to your local machine.

3. **Data Preparation**:
   - Ensure you have the required input data:
     - Terrain data (`altum_terrain`)
     - Climate data (`climate_altum`)
     - Vegetation indices data (`altum_ndvi_savi`)
   - The data should be in the correct format and accessible by the provided functions.
   - Ensure you have ground truth data in a CSV format accessible by the `GetCSVDataAsArray` module.

4. **Training**:
   - Run the `train_model.py` script to train the Random Forest regression model.
   - The trained model will be saved as `trained_rf_model.joblib`.

5. **Prediction**:
   - Load the trained model using `joblib.load('trained_rf_model.joblib')`.
   - Prepare your new data using raster files as input, processed through the provided functions.
   - Use the `predict()` method of the loaded model to make predictions on the new data.

## Files

- `train_model.py`: Python script for training the Random Forest regression model.
- `GetInputFiles.py`: Python script containing functions to get paths to input files.
- `GetFeaturesAndGroundTruth.py`: Python script containing functions to extract features and ground truth data.

## Data Handling

- **GetCSVDataAsArray.py**: Module to retrieve ground truth data from a CSV file and convert it into an array format.
- **GetFeaturesAndGroundTruth.py**: Module to extract feature values and ground truth data from raster files.

## Notes

- The trained model is saved as a joblib file (`trained_rf_model.joblib`).
- Ensure that the input data format and preprocessing steps match those used during training.
- For any issues or questions, please contact [maintainer_email@example.com].
