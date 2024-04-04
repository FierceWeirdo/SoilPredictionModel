import pandas as pd

# Getting data from csv file into an array

def get_ground_truth_array():
    csv_file = "SoilPredictionModel/fieldDataBCAlbers.csv" #path to csv file
    df = pd.read_csv(csv_file)
    data_array = df[['Easting', 'Northing', 'Altitude', 'Bare_Ground']].values.tolist()
    return data_array

