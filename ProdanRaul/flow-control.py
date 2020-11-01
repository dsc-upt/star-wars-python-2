import json

laptops = {
    "HP": "4 RAM",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    "cats": ['56', 57],
    "dictionary":
        {
            "ion": 56,
            "ana": 0
            # ("Merge", 'Pull'): "Request"
        }
}


for item in laptops.items():
    print(item)

for key, value in laptops.items():
    print(key, "----", value)

for value in laptops.values():
    if type(value) is dict:
        print(json.dumps(value, indent=4))
