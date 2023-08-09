# Function to read properties from a file and return a dictionary
def read_properties_file(file_path):
    properties_dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            key, value = line.split('=', 1)
            properties_dict[key] = value
    return properties_dict

# Read properties from the two files
properties_dict1 = read_properties_file('config3a.properties')
properties_dict2 = read_properties_file('config3b.properties')

# Compare the dictionaries
print("Items present in both files:")
for key in properties_dict1:
    if key in properties_dict2:
        value1 = properties_dict1[key]
        value2 = properties_dict2[key]
        if value1 == value2:
            print(f"{key}: {value1}")
        else:
            print(f"{key}: Value differs: {value1} (file 1) vs {value2} (file 2)")

print("\nItems present only in file 1:")
for key in properties_dict1:
    if key not in properties_dict2:
        print(f"{key}: {properties_dict1[key]}")

print("\nItems present only in file 2:")
for key in properties_dict2:
    if key not in properties_dict1:
        print(f"{key}: {properties_dict2[key]}")
