import json
import pandas as pd

with open('data.json') as f:
    data = json.load(f)

print(data[0]['name'])


data = {
    "name": "John",
    "age": 25
}

with open("data_new.json", "w") as file:
    json.dump(data, file, indent=4)
 

data = {
    "name": ["John"],
    "age": [25]
}

df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
