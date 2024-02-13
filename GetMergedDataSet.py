import rasterio
from GetCSVDataAsArray import get_ground_truth_array

ground_truth_data = get_ground_truth_array()
merged_data_set = []

def match_raster_values(raster_file_paths):

    src = rasterio.open(raster_file)
    raster_coords = [(point[0], point[1]) for point in ground_truth]
    sampled_values = list(src.sample(raster_coords))
    src.close()
    
    for i, point in enumerate(ground_truth):
        if len(sampled_values[i]) > 0: 
            merged_data_set.append(sampled_values[i][0])
        else:
            merged_data_set.append('nothing') 

    return merged_data_set
    
merged_data_set = match_raster_values('SoilPredictionModel/terrain_rasters/Altum/Altum_Aspect.tif')
merged_data_set = match_raster_values('SoilPredictionModel/terrain_rasters/Altum/Altum_Aspect.tif')
print(ground_truth_data)