import json

with open('./data/output.json') as file:
    data = json.load(file)
print(data)