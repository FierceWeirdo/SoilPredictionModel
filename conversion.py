from pyproj import Proj, transform
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

file_path = 'Downloads/fieldSurvey.csv'

df = pd.read_csv(file_path)
for index, row in df.iterrows():
    element_iatX = df.iat[index, 0] # Row 0, Column 0
    element_iatY = df.iat[index, 1] # Row 0, Column 0
    latitude = element_iatX
    longitude = element_iatY
    bc_albers = Proj(init='epsg:3005')
    bc_albers_x, bc_albers_y = transform(Proj(init='epsg:4326'), bc_albers, longitude, latitude)
    print(bc_albers_y)
    # print("BC Albers Y:", bc_albers_y)

