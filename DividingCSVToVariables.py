import csv

input_file = 'Climate_Vars_2029_Except_No_Data.csv'
output_file = 'Climate_MWMT_2029.csv'

columns_to_keep = [0, 1, 4]  # Column indices (0-based) to keep: column1, column2, column4
#Easting,Northing,Elevation,MAT,MWMT,MCMT,TD,MAP,MSP,AHM,SHM,DD_0,DD5,DD_18,DD18,NFFD,bFFP,eFFP,FFP,PAS,EMT,EXT,MAR,Eref,CMD,RH,CMI,DD1040

with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
    reader = csv.reader(csv_in)
    writer = csv.writer(csv_out)
    
    for row in reader:
        selected_columns = [row[i] for i in columns_to_keep if i < len(row)]
        writer.writerow(selected_columns)
