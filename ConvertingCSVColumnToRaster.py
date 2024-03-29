# import pandas as pd
# from osgeo import gdal, osr, ogr

# # Read CSV file
# csv_file = 'Climate_Vars_2029_Except_.csv'
# data = pd.read_csv(csv_file)

# # Define raster parameters
# output_raster = 'Climate_MAT.tif'
# x_min, x_max = data['Easting'].min(), data['Easting'].max()
# y_min, y_max = data['Northing'].min(), data['Northing'].max()
# pixel_size = 50  # Set your desired pixel size
# cols = int((x_max - x_min) / pixel_size)
# rows = int((y_max - y_min) / pixel_size)
# origin_x = x_min
# origin_y = y_max

# # Create raster
# driver = gdal.GetDriverByName('GTiff')
# out_raster = driver.Create(output_raster, cols, rows, 1, gdal.GDT_Float32)
# out_raster.SetGeoTransform((origin_x, pixel_size, 0, origin_y, 0, -pixel_size))

# # Create spatial reference
# spatial_ref = osr.SpatialReference()
# spatial_ref.ImportFromEPSG(4326)  # Assuming WGS84, change if necessary
# out_raster.SetProjection(spatial_ref.ExportToWkt())

# # Write MAT data to raster
# band = out_raster.GetRasterBand(1)
# band.WriteArray(data['MAT'].values.reshape(rows, cols))

# # Close raster
# band.FlushCache()
# out_raster.FlushCache()

# # Apply the raster profile of another raster (ALTUM_DEM)
# altum_dem = 'SoilPredictionModel/terrain_rasters/Altum/Altum_DEM.tif'
# src_ds = gdal.Open(altum_dem)

# if src_ds:
#     gdal.Warp(output_raster, out_raster, format='GTiff', srcSRS=src_ds.GetProjection())
#     src_ds = None

# print("Raster file created successfully.")





# import numpy as np
# import pandas as pd
# import rasterio
# from rasterio.transform import from_origin
# from rasterio.enums import Resampling

# # Read the CSV file
# data = pd.read_csv('Climate_Vars_2029_Except_No_Data.csv')
# print('Done reading CSV')
# # Extract Easting, Northing, and MAT values
# easting = data['Easting']
# northing = data['Northing']
# mat = data['MAT']

# # Define the resolution of your raster
# pixel_size_x = 0.5
# pixel_size_y = -0.5  # Negative because Northings decrease as we go down
# resolution = (pixel_size_x, pixel_size_y)

# # Calculate the width and height of the raster
# width = 18552
# height = 10351

# # Create an empty array to store MAT values
# mat_array = np.empty((height, width), dtype=np.float32)
# print('Done with empty mat array')

# # Populate the MAT array
# for x, y, value in zip(easting, northing, mat):
#     col = int((x - easting.min()) / abs(pixel_size_x))
#     row = int((northing.max() - y) / abs(pixel_size_y))
#     mat_array[row, col] = value

# # Define the upper left corner coordinates
# x_min = easting.min()
# y_max = northing.max()

# # Define the transformation for GeoTIFF
# transform = from_origin(x_min, y_max, pixel_size_x, pixel_size_y)

# # Define metadata for the GeoTIFF file
# meta = {
#     'driver': 'GTiff',
#     'count': 1,
#     'dtype': 'float32',
#     'width': width ,
#     'height': height,
#     'crs': 'EPSG:4326',
#     'transform': transform
# }

# # Write the GeoTIFF file
# with rasterio.open('Climate_MAT.tif', 'w', **meta) as dst:
#     dst.write(mat_array, 1)

# print("GeoTIFF file created successfully.")

# import pandas as pd
# import numpy as np
# import rasterio
# from rasterio.features import rasterize
# from rasterio.transform import from_origin

# # Read CSV file
# print("Reading CSV file...")
# data = pd.read_csv('Climate_Vars_2029_Except_No_Data.csv')
# print("CSV file read successfully.")

# # Define raster parameters
# pixel_size_x = 0.5
# pixel_size_y = -0.5
# width = 18552
# height = 10351
# transform = from_origin(data['Easting'].min(), data['Northing'].max(), pixel_size_x, pixel_size_y)

# # Create an empty array to store MAT values
# mat_array = np.zeros((height, width), dtype=np.float32)

# # Create a boolean mask for rasterization
# mask = np.zeros((height, width), dtype=bool)
# for x, y in zip(data['Easting'], data['Northing']):
#     col = int((x - data['Easting'].min()) / abs(pixel_size_x))
#     row = int((data['Northing'].max() - y) / abs(pixel_size_y))
#     mask[row, col] = True

# # Rasterize points to populate the array
# print("Rasterizing points...")
# rasterized = rasterize(
#     [(x, y) for x, y in zip(data['Easting'], data['Northing'])],
#     out_shape=(height, width),
#     transform=transform,
#     fill=data['MAT'].values,
#     default_value=0,
#     all_touched=True,
#     invert=True,
#     mask=mask
# )
# print("Points rasterized.")

# # Assign rasterized values to the MAT array
# print("Assigning rasterized values to the MAT array...")
# mat_array[rasterized != 0] = rasterized[rasterized != 0]
# print("Rasterized values assigned to the MAT array.")

# # Write the GeoTIFF file
# print("Writing GeoTIFF file...")
# with rasterio.open('Climate_MAT.tif', 'w', driver='GTiff', dtype='float32', count=1, width=width, height=height,
#                    crs='EPSG:3005', transform=transform) as dst:
#     dst.write(mat_array, 1)
# print("GeoTIFF file created successfully.")

import numpy as np
import csv
import rasterio
from rasterio.transform import from_origin
from rasterio.enums import Resampling

def convert_csv_to_tiff(csv_file, tiff_file):
    # Read CSV
    eastings = []
    northings = []
    mats = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if exists
        for row in reader:
            eastings.append(float(row[0]))
            northings.append(float(row[1]))
            mats.append(float(row[2]))

    # Determine extent
    min_easting = min(eastings)
    min_northing = min(northings)
    max_easting = max(eastings)
    max_northing = max(northings)
    width = int((max_easting - min_easting) / 0.5) + 1
    height = int((max_northing - min_northing) / 0.5) + 1

    # Create empty array for data
    data = np.zeros((height, width), dtype=np.float32)

    # Populate data array with MAT values
    for i in range(len(eastings)):
        x_index = int((eastings[i] - min_easting) / 0.5)
        y_index = int((max_northing - northings[i]) / 0.5)
        data[y_index][x_index] = mats[i]

    # Create GeoTIFF
    transform = from_origin(min_easting, max_northing, 0.5, 0.5)  # Assuming pixel size is 0.5 as mentioned
    profile = {
        'driver': 'GTiff',
        'width': width,
        'height': height,
        'count': 1,
        'dtype': 'float32',
        'crs': 'EPSG:3005',
        'transform': transform,
        'compress': 'lzw',
        'nodata': None
    }
    with rasterio.open(tiff_file, 'w', **profile) as dst:
        dst.write(data, 1)

# Example usage
csv_file = "MAT2029.csv"
tiff_file = "MAT_2029.tif"
convert_csv_to_tiff(csv_file, tiff_file)
