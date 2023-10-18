import json

# Specify the input and output file paths
input_file_path = "wrong_comms.json"
output_file_path = "wrong_comms_prepped.json"

# Function to remove text between ##COMMAND: and ##SYSTEM:
def remove_command_and_system(json_obj):
    for key in list(json_obj.keys()):
        if '##COMMAND:' in json_obj[key]:
            try:
                start = json_obj[key].index('##COMMAND:')
                end = json_obj[key].index('##SYSTEM:') + len('##SYSTEM:')
                json_obj[key] = json_obj[key][:start] + "##SYSTEM:"  + json_obj[key][end:]
            except:
                pass
    return json_obj

# Read the input JSON file
with open(input_file_path, 'r') as input_file:
    data = json.load(input_file)

# Process the JSON objects and remove text
modified_data = [remove_command_and_system(json_obj) for json_obj in data]

# Write the modified JSON objects to the output file
with open(output_file_path, 'w') as output_file:
    json.dump(modified_data, output_file, indent=4)

print(f"Text between ##COMMAND: and ##SYSTEM: removed. Output saved to {output_file_path}")
