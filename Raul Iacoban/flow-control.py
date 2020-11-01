import json
#from json import dumps

laptops = {
    "HP": "4 ram",
    "Apple": 1,
    "Dell": 2
}

laptops.update({"Lenovo": 3})
print(json.dumps(laptops, indent=1))

for key, value in laptops.items():
    print(key)
    print(value)

for key in laptops.keys():
    print(key)