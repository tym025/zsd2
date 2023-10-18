import json
import random
import os
from datetime import datetime

# Load the data from the input file
with open('data//20231014134937//output.json', 'r') as file:
    data = json.load(file)

# Define the split ratio
split_ratio = 0.85

# Shuffle the data randomly
random.shuffle(data)

# Calculate the number of samples for training and validation
total_samples = len(data)
num_train_samples = int(split_ratio * total_samples)

# Split the data into training and validation sets
train_data = data[:num_train_samples]
valid_data = data[num_train_samples:]

# Create a folder with the current date and time as the name
current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
output_folder = os.path.join("data", current_datetime)
os.makedirs(output_folder, exist_ok=True)

# Create training and validation files inside the folder
train_file_path = os.path.join(output_folder, 'output_train.json')
valid_file_path = os.path.join(output_folder, 'output_valid.json')

with open(train_file_path, 'w') as train_file:
    json.dump(train_data, train_file, indent=4)

with open(valid_file_path, 'w') as valid_file:
    json.dump(valid_data, valid_file, indent=4)

print(f"Training data saved to '{train_file_path}' ({len(train_data)} samples).")
print(f"Validation data saved to '{valid_file_path}' ({len(valid_data)} samples).")
