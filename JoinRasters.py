import rasterio
import numpy as np

# Open the two raster files
with rasterio.open('predicted_soil_probability_5.tif') as src1:
    with rasterio.open('predicted_soil_probability_6.tif') as src2:
        
        # Get the metadata of the first raster
        meta = src1.meta
        
        # Determine the new height and width
        new_height = src1.height + src2.height
        new_width = max(src1.width, src2.width)
        
        # Create an empty array for the combined data
        combined_data = np.zeros((new_height, new_width), dtype=src1.dtypes[0])
        
        # Read and write data from the first raster
        combined_data[:src1.height, :src1.width] = src1.read(1)
        
        # Calculate the offset for the second raster
        y_offset = src1.height
        
        # Read and write data from the second raster
        combined_data[y_offset:y_offset+src2.height, :src2.width] = src2.read(1)
        
        # Update metadata with the new dimensions
        meta.update(height=new_height, width=new_width)
        
        # Create a new raster file for the combined raster
        with rasterio.open('Altum_Soil_Prob.tif', 'w', **meta) as dst:
            
            # Write the combined data to the new raster file
            dst.write(combined_data, 1)
