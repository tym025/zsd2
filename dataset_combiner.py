import json

# Define input and output file paths
input_file_path = 'output.json'  # Replace with your input file
output_file_path = 'data//20231014134937//output.json'  # Replace with your output file

# Read the input JSON file
with open(input_file_path, 'r') as input_file:
    data = json.load(input_file)

# Process and modify the data
for item in data:
    input_text = item["input"]
    output_text = item["output"]
    combined_text = f"{input_text} {output_text} ##END"
    item["combined"] = combined_text

# Write the modified data to the output JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(data, output_file, indent=4)

print(f"Output JSON data has been written to {output_file_path}")
