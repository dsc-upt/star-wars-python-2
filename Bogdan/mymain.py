import json
#javascript object notation
# Dictionaries: {key:value, key1:value1, ... } immutable values(string, touples, int, float)
laptops= {
    "HP": "4 ran",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 4,
}
print(laptops)

laptops.update({"new_value":"from update man"})
print(laptops)

print(laptops.keys())
x = json.dumps(laptops, indent=4)
print(x)



