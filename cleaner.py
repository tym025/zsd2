import unicodedata

def remove_non_ascii(input_string):
    # Create an empty string to store the result
    result = ""

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a non-ASCII character
        if ord(char) > 127:
            # Try to normalize the character to its closest ASCII equivalent
            normalized_char = unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').decode('utf-8')
            # If the normalization was successful, use the normalized character
            if normalized_char:
                result += normalized_char
            else:
                # If normalization failed, replace with a placeholder
                result += '[?]'
        else:
            # If the character is already ASCII, keep it as is
            result += char

    return result

# Function to process a file and replace non-ASCII characters
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    normalized_content = remove_non_ascii(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(normalized_content)

# Example usage
input_file = "input.txt"
output_file = "output.txt"
process_file(input_file, output_file)
