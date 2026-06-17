import json

# Open and load the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the content
print(data)
print(data['name'])  