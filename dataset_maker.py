import json

# Input and output file paths
csv_file_path = "llmfinetune_cities.csv"
json_file_path = "output.json"

# Output JSON data
json_data = []

# Open the CSV file and read it line by line
with open(csv_file_path, "r") as csv_file:
    for line in csv_file:
        # Remove the newline character at the end of the line
        line = line.rstrip("\n")

        # Split the line into its components
        components = line.split(" ##")
        print(components)

        # Process each line according to the provided rules
        if "SYSTEM" in line:
            # Split the 'SYSTEM' component into 'SYSTEM' and 'RESPONSE'
            print(components)
            user = components[0]
            comm = components[1]
            system = components[2]
            response = components[3]
            
            # Create two separate elements for this line
            json_data.append({
                "input": user,
                "output": "##" + comm
            })
            json_data.append({
                "input": user + " ##" + comm + " ##" + system,
                "output": "##" + response
            })
        else:
            # Create one element for this line
            json_data.append({
                "input": components[0],
                "output": "##" + components[1] + " ##" + components[2]
            })

# Convert the JSON data to a string
json_str = json.dumps(json_data, indent=4)

# Write the JSON string to the output file
with open(json_file_path, "w") as json_file:
    json_file.write(json_str)
