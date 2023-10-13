import json
import random

# Load the data from the input file
with open('output.json', 'r') as file:
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

# Create training and validation files
with open('output_train_updated.json', 'w') as train_file:
    json.dump(train_data, train_file, indent=4)

with open('output_valid_updated.json', 'w') as valid_file:
    json.dump(valid_data, valid_file, indent=4)

print(f"Training data saved to 'output_train_updated.json' ({len(train_data)} samples).")
print(f"Validation data saved to 'output_valid_updated.json' ({len(valid_data)} samples).")
