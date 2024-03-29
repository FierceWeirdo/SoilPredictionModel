import pandas as pd
import numpy as np
import rasterio

# Read CSV file
csv_file = 'Climate_Vars_2029_Except_No_Data.csv'
data = pd.read_csv(csv_file)
print("Read the file")

# Define output raster parameters based on another GeoTIFF file
reference_tiff = 'SoilPredictionModel/terrain_rasters/Altum/Altum_DEM.tif'  # Path to the reference GeoTIFF file
with rasterio.open(reference_tiff) as src_ref:
    pixel_size_x, pixel_size_y = src_ref.res
    if pixel_size_x <= 0 or pixel_size_y <= 0:
        raise ValueError("Invalid pixel sizes detected in the reference GeoTIFF.")
    origin_x, origin_y = src_ref.bounds.left, src_ref.bounds.top
    crs = src_ref.crs

# Calculate number of rows and columns based on the extent of the CSV data and pixel size
x_min, x_max = data['Easting'].min(), data['Easting'].max()
y_min, y_max = data['Northing'].min(), data['Northing'].max()

# Adjust the number of columns and rows based on the extent of the CSV data and pixel size
cols = int((x_max - x_min) / pixel_size_x) + 1  # Adding 1 to ensure coverage of all points
rows = int((y_max - y_min) / pixel_size_y) + 1

# Create empty raster
raster_data = np.zeros((rows, cols))

# Fill raster with MAT values from CSV
for index, row in data.iterrows():
    col_index = int((row['Easting']) / pixel_size_x)
    row_index = int((row['Northing']) / pixel_size_y)
    try:
        raster_data[row_index, col_index] = row['MAT']
    except IndexError:
        print(f"Warning: Point at coordinates ({row['Easting']}, {row['Northing']}) is out of bounds.")

# Save raster as GeoTIFF
output_raster = 'Climate_MAT.tif'
profile = {
    'driver': 'GTiff',
    'dtype': rasterio.float32,
    'count': 1,
    'width': cols,
    'height': rows,
    'crs': crs,
    'transform': rasterio.transform.from_origin(x_min, y_max, pixel_size_x, pixel_size_y),  # Using x_min and y_max as origin
    'compress': 'lzw',
    'nodata': -9999  # Define nodata value as needed
}

with rasterio.open(output_raster, 'w', **profile) as dst:
    dst.write(raster_data.astype(rasterio.float32), 1)

print("Raster file created successfully.")
