# Getting data from csv file into an array
import pandas as pd

def get_ground_truth_array():
    csv_file = "SoilPredictionModel/fieldDataBCAlbers.csv" #path to csv file
    df = pd.read_csv(csv_file)
    data_array = df[['Easting', 'Northing', 'Altitude', 'Bare_Ground']].values.tolist()
    return data_array

