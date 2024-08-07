import rasterio
import numpy as np

# Combining raster files
with rasterio.open('future_2034_first_half.tif') as src1:
    with rasterio.open('future_2034_second_half.tif') as src2:
        
        meta = src1.meta
        
        new_height = src1.height + src2.height
        new_width = max(src1.width, src2.width)
        
        combined_data = np.zeros((new_height, new_width), dtype=src1.dtypes[0])
        
        combined_data[:src1.height, :src1.width] = src1.read(1) # adding data from first raster to array
      
        y_offset = src1.height 
        
        combined_data[y_offset:y_offset+src2.height, :src2.width] = src2.read(1) #second raster data
        
        meta.update(height=new_height, width=new_width)
        
        #Creating new raster file
        with rasterio.open('Future_Prediction_2034.tif', 'w', **meta) as dst:
         
            dst.write(combined_data, 1)
