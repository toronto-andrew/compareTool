# Open the properties file
with open('config2.properties', 'r') as file:
    # Read lines from the file
    lines = file.readlines()

# Loop through the lines and print key-value pairs
print("Properties:")
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace
    if line:  # Skip empty lines
        key, value = line.split('=', 1)
        print(f"{key}: {value}")
