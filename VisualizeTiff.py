import matplotlib.pyplot as plt
import rasterio

# Used to visualize changes in the three files. Still in work

# Load the first TIFF file
tiff_file_1 = 'Altum_Soil_Prob.tif'

# Define the window for the first file (in terms of pixel coordinates)
window = ((2500, 2700), (16200, 16500))  # Example window, adjust as needed

# Open the first TIFF file
with rasterio.open(tiff_file_1) as src1:
    # Read the data for the specified window
    data_window_1 = src1.read(1, window=window)

    # Plotting the first raster data
    plt.plot(data_window_1.flatten(), color='blue', label='Current Occurrence')

# Load the second TIFF file
tiff_file_2 = 'Future_Prediction_2029.tif'

# Open the second TIFF file
with rasterio.open(tiff_file_2) as src2:
    # Read the data for the specified window
    data_window_2 = src2.read(1, window=window)

    # Plotting the second raster data
    plt.plot(data_window_2.flatten(), color='red', label='2029 Occurrence')

tiff_file_3 = 'Future_Prediction_2034.tif'

# Open the third TIFF file
with rasterio.open(tiff_file_3) as src3:
    # Read the data for the specified window
    data_window_3 = src3.read(1, window=window)

    # Plotting the second raster data
    plt.plot(data_window_3.flatten(), color='green', label='2034 Occurrence')

# Adding labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Chart of Two Raster Files (Windows)')
plt.legend()  # Adding legend to distinguish between the two raster files
plt.show()
