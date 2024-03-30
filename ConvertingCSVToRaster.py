import numpy as np
import csv
import rasterio
from rasterio.transform import from_origin, Affine 
from rasterio.enums import Resampling
from rasterio.crs import CRS

import os

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

    width = 18552
    height = 10351

    # Create empty array for data
    data = np.full((height, width), -99999.0, dtype=np.float32)

    # Populate data array with MAT values
    for i in range(len(eastings)):
        x_index = int((eastings[i] - 1358941) / 0.5)
        y_index = int((656280 - northings[i]) / 0.5)
        data[y_index][x_index] = mats[i]    

    with rasterio.open('SoilPredictionModel/terrain_rasters/Altum/Altum_DEM.tif') as src:
        transform = src.transform
        width = src.width
        height = src.height
        crs = src.crs
    # Create GeoTIFF
    profile = {
        'driver': 'GTiff',
        'dtype': 'float32',
        'nodata': -99999.0,
        'width': width, #18552,
        'height': height, #10351,
        'count': 1,
        'crs':crs, #CRS.from_epsg(3005),
        'transform': transform, #Affine(0.5, 0.0, 1358941.0, 0.0, -0.5, 656280.0),
        'blockysize': 1,
        'tiled': False,
        'compress': 'lzw',
        'interleave': 'band'
    }
    with rasterio.open(tiff_file, 'w', **profile) as dst:
        dst.write(data, 1)


output_folder = 'output/'
for filename in os.listdir(output_folder):
    if filename.endswith(".csv"):
        csv_file = os.path.join(output_folder, filename)
        tiff_file = os.path.splitext(csv_file)[0] + ".tif" 
        convert_csv_to_tiff(csv_file, tiff_file)