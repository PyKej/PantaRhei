import csv

# Define the path to your input CSV file
input_csv_file_path = 'csv-files/firewall-logs.csv'
# Define the path to your output CSV file
output_csv_file_path = 'csv-files/repaired-file.csv'

# Function to check if a value is enclosed in double quotes
def is_enclosed_in_quotes(value):
    return value.startswith('"') and value.endswith('"')

# List to store corrected rows
corrected_rows = []

# Open and read the CSV file
with open(input_csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Assuming the first row is the header
    corrected_rows.append(header)  # Add header to corrected rows

    # Check each row
    for row in csv_reader:
        if len(row) > 9:
            user_column_index = header.index("User Agent")  # Adjust the column name if needed
            datetime_column_index = len(row) - 1 # get the last column index

            # Check if the User Agent column is not enclosed in double quotes
            if not is_enclosed_in_quotes(row[user_column_index]):
                user_column_value = ' '.join(row[user_column_index:datetime_column_index])
                row[user_column_index] = f'"{user_column_value}"'
                # Remove other columns in the range
                del row[user_column_index+1:datetime_column_index]
                
        corrected_rows.append(row)

# Write the corrected rows to a new CSV file
with open(output_csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(corrected_rows)

print(f"Corrected CSV file has been created: {output_csv_file_path}")
