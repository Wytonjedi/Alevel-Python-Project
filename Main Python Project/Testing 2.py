import json
with open("package.json") as json_file:
    data = json.load(json_file)
print(data["ceaser"])
