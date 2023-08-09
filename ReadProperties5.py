# Open the properties file
with open('config2.properties', 'r') as file:
    # Read lines from the file
    lines = file.readlines()

# Create an empty dictionary to store key-value pairs
properties_dict = {}

# Loop through the lines and store key-value pairs in the dictionary
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace
    if line:  # Skip empty lines
        key, value = line.split('=', 1)
        properties_dict[key] = value

# Print the dictionary
print("Properties Dictionary:")
for key, value in properties_dict.items():
    print(f"{key}: {value}")
