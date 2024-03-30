import csv

input_file = 'Climate_Vars_2029_Except_No_Data.csv'
output_folder = 'output/'

columns_to_keep = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]  

with open(input_file, 'r') as csv_in:
    reader = csv.reader(csv_in)
    headers = next(reader)  # Read the header row
    
    for i in columns_to_keep:
        output_file = f"{output_folder}{headers[i]}_2029.csv"  # Output file name based on the column name
        with open(output_file, 'w', newline='') as csv_out:
            writer = csv.writer(csv_out)
            # Write header row
            writer.writerow(["Easting", "Northing", headers[i]])  
            # Write data rows
            csv_in.seek(0)  # Reset the file pointer to the beginning
            next(csv_in)  # Skip the header row
            for row in reader:
                writer.writerow([row[0], row[1], row[i]])
        csv_in.seek(0)  # Reset the file pointer to the beginning for the next iteration
        next(csv_in)  # Skip the header row for subsequent iterations
