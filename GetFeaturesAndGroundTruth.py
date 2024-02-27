import rasterio
from GetCSVDataAsArray import get_ground_truth_array
import numpy as np

ground_truth_data = get_ground_truth_array()

def get_all_raster_values_for_ground_truth(raster_paths_array):
    coord_pairs = []

    # Extracting coordinates from ground_truth_data
    for element in ground_truth_data:
        coord_pairs.append(element[:2])

    # Storing sampled values for each raster
    all_sampled_values = []

    for raster_file_path in raster_paths_array:
        src = rasterio.open(raster_file_path)
        sampled_values = list(src.sample(coord_pairs))
        src.close()
        all_sampled_values.append(sampled_values)

    # Combining sampled values into merged_data_set
    feature_values_array = []
    for sampled_values in zip(*all_sampled_values):
        values = []
        for vals in sampled_values:
            if len(vals) > 0:
                values.append(vals[0])
            else:
                values.append('nothing')
        feature_values_array.append(values)
    
    return np.array(feature_values_array)

def get_all_bare_ground_values_as_array():
    bare_ground_values = []
    for element in ground_truth_data:
        bare_ground_values.append(element[3])
    return np.array(bare_ground_values)