import json

# Load the JSON data from the file
with open('output_train.json', 'r') as file:
    data = json.load(file)

# Create a new list to store the transformed data
transformed_data = []

# Iterate through each dictionary in the input data
for item in data:
    # Extract the "input" and "output" fields
    input_text = item["input"]
    output_text = item["output"]

    # Create a new dictionary with the "text" key
    transformed_item = {"text": input_text}
    transformed_data.append(transformed_item)

    transformed_item = {"text": output_text}
    transformed_data.append(transformed_item)

# Save the transformed data to a new JSON file
with open('output_data.json', 'w') as file:
    json.dump(transformed_data, file, indent=2)