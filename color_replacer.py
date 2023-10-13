import csv
import random

yacht_rooms = [
    "Santorini",
    "Maui",
    "Ibiza",
    "Maldives",
    "Seychelles",
    "Phuket",
    "Hawaii",
    "Bali",
    "Amsterdam",
    "Prague",
    "Rome",
    "Los Angeles",
    "Hong Kong",
    "Machu Picchu",
    "Santorini",
    "Easter Island",
    "Svalbard",
    "Cape Town",
    "Honolulu",
    "Barcelona",
    "Istanbul",
    "Auckland",
    "Bora Bora"
]

input_csv_file = 'llmfinetune_dates.csv'
output_csv_file = 'llmfinetune_cities.csv'
delimiter = ','  # Change this to the appropriate delimiter if your CSV file uses a different one.

with open(input_csv_file, 'r', newline='') as csvfile_input, open(output_csv_file, 'w', newline='') as csvfile_output:
    reader = csv.reader(csvfile_input, delimiter=delimiter)
    writer = csv.writer(csvfile_output, delimiter=delimiter)
    
    for row in reader:
        modified_row = [cell.replace('$CITY$', random.choice(yacht_rooms)) for cell in row]
        writer.writerow(modified_row)

csvfile_input.close()
csvfile_output.close()
