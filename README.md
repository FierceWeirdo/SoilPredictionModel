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


## Note

- Make sure to replace the paths and filenames in the scripts with your actual file paths and names.
- Ensure that the CSV file and raster files are properly formatted and accessible.
- Adjust parameters such as the number of estimators, maximum depth, and minimum samples split according to your requirements for model training.


## Note for Running Prediction Model

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
- **Rhythm Chauhan**
  - [Email her](mailto:eyeamrhythm2003@gmail.com)

- **Bir Inder Singh**
  - [Email her](mailto:virkbunny13@gmail.com)

- **Japkirat Singh**
  - [Email her](mailto:japkirat66@gmail.com)
