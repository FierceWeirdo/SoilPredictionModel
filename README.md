# Soil Prediction Model

This repository contains a set of Python scripts for soil prediction using raster data and machine learning techniques. The following sections provide an overview of the structure and usage of these scripts.

## Structure

The repository is organized into several modules:

1. **GetCSVDataAsArray**: Module to extract ground truth data from a CSV file containing soil data.
2. **GetInputFiles**: Module to retrieve paths to input raster files required for soil prediction.
3. **GetFeaturesAndGroundTruth**: Module to extract raster values for ground truth coordinates and bare ground values.
4. **SoilPredictionModel**: Module to train a Random Forest Regressor model for soil prediction using extracted features and ground truth data.
5. **GenerateTiffFile**: Module to generate a GeoTIFF file containing predicted soil probability.

## Usage

To utilize the functionality provided by this repository, follow these steps:

1. **Extract Ground Truth Data**:
   - Use the `get_ground_truth_array()` function in the `GetCSVDataAsArray` module to extract ground truth data from a CSV file.

2. **Retrieve Input Raster Paths**:
   - Use the `get_paths_to_files(name_of_files_needed)` function in the `GetInputFiles` module to retrieve paths to input raster files based on the required categories such as altitude, terrain, index, or climate.

3. **Extract Features and Ground Truth**:
   - Use the functions in the `GetFeaturesAndGroundTruth` module to extract raster values for ground truth coordinates and bare ground values.

4. **Train Soil Prediction Model**:
   - Use the `SoilPredictionModel` module to train a Random Forest Regressor model for soil prediction. Ensure that you have extracted features and ground truth data before training the model.

5. **Generate GeoTIFF File**:
   - Use the `GenerateTiffFile` module to generate a GeoTIFF file containing predicted soil probability based on the trained model and input raster files.

## Dependencies

Ensure you have the following dependencies installed:

- pandas
- numpy
- rasterio
- scikit-learn (sklearn)
- joblib

You can install these dependencies via pip:

`pip install pandas numpy rasterio scikit-learn joblib`

## Creating and Using Your Own Prediction Model

You can use this code to create your own soil prediction model and save it for future use. Follow these steps:

1. **Prepare Your Data**:
   - Ensure you have your ground truth data in a CSV file formatted similarly to `fieldDataBCAlbers.csv`. Update the file path in the `GetCSVDataAsArray` module if needed.
   - Organize your raster files into appropriate folders according to terrain, index, and climate categories. Update the file paths in the `GetInputFiles` module if needed.

2. **Extract Features and Ground Truth**:
   - Use the provided modules (`GetCSVDataAsArray`, `GetInputFiles`, and `GetFeaturesAndGroundTruth`) to extract features and ground truth data from your CSV file and raster files.

3. **Train Your Model**:
   - Utilize the `SoilPredictionModel` module to train your model. Adjust parameters such as the number of estimators, maximum depth, and minimum samples split based on your data and requirements.

4. **Save Your Model**:
   - Once your model is trained, save it using the `joblib.dump()` function provided in the `SoilPredictionModel` module. This will save your trained model as a binary file that can be loaded and used for predictions later.

5. **Predict Soil Values**:
   - Use the saved model to predict soil values for new raster data. Follow the instructions provided in the `GenerateTiffFile` module to generate predicted soil probability GeoTIFF files using your trained model.

Remember to update file paths, parameters, and other configurations according to your specific data and requirements.

## Note for Running Our Pre-Trained Prediction Model

To run the prediction model on a set of rasters, ensure that the following files are fed to the model (note any size of land can be used to run depending on your computation capabilities) in the same order (as that is how the model was trained):

- 'Altum_Aspect.tif'
- 'Altum_Convergence.tif'
- 'Altum_DAH.tif'
- 'Altum_DEM.tif'
- 'Altum_General_curvature.tif'
- 'Altum_H_Overland_Dist.tif'
- 'Altum_Insolation_Diffuse.tif'
- 'Altum_Insolation_Direct.tif'
- 'Altum_MRRTF.tif'
- 'Altum_MRVBF.tif'
- 'Altum_Openness_Neg.tif'
- 'Altum_Openness_Pos.tif'
- 'Altum_Overland_Dist.tif'
- 'Altum_Slope.tif'
- 'Altum_Total_curvature.tif'
- 'Altum_TPI.tif'
- 'Altum_TRI.tif'
- 'Altum_TWI.tif'
- 'Altum_V_Dist_to_cnetwork.tif'
- 'Altum_V_Overland_Dist.tif'
- 'Altum_Year_2022Y_EMT.tif'
- 'Altum_NDVI.tif'
- 'Altum_SAVI.tif'

Ensure that the paths to these files are correctly provided when running the prediction model.



## Contributors
- **Rhythm Chauhan**: [Email Rhythm](mailto:eyeamrhythm2003@gmail.com)

- **Bir Inder Singh**: [Email Bir](mailto:virkbunny13@gmail.com)

- **Japkirat Singh**: [Email Japkirat](mailto:japkirat66@gmail.com)
