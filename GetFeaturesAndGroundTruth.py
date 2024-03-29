import rasterio
from GetCSVDataAsArray import get_ground_truth_array
import numpy as np

ground_truth_data = get_ground_truth_array()

def get_all_raster_values_for_ground_truth(raster_paths_array):
    coord_pairs = []

    # Extracting coordinates from ground_truth_data
    for element in ground_truth_data:
        coord_pairs.append(element[:2])
    print (coord_pairs)

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
    print (np.array(bare_ground_values))
    return np.array(bare_ground_values)

import csv
import numpy as np
import rasterio

def get_all_raster_values_for_ground_truth_including_climate(paths_array, csv_file_path):
    coord_pairs = []

    # Extracting coordinates from ground_truth_data
    for element in ground_truth_data:
        coord_pairs.append(element[:2])
    print(coord_pairs)

    # Read CSV file
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_rows = [row for row in reader]

    # Filter rows based on matching coord pairs
    matching_rows = []
    for row in data_rows:
        if (row['Easting'], row['Northing']) in coord_pairs:
            matching_rows.append(row)

    # Transpose matching_rows
    transposed_matching_rows = list(map(list, zip(*[row.values() for row in matching_rows])))
    print(transposed_matching_rows)

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

    feature_values_array = np.concatenate((feature_values_array, transposed_matching_rows), axis=1)

    return np.array(feature_values_array)