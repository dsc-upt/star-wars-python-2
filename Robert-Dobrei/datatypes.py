import json  #javascript

# Tuples: (), este o lista, e immutable, se comporta ca o constanta

cats = (6, 'Anakin')

print(cats[1])

# Dictionaries: {}
laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
}
print(laptops)

laptops.update({"new value": "from update method"})
print(json.dumps(laptops))
print()
print(laptops.values())
print(laptops.keys())

