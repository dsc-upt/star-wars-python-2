import json

print("Hello world!")

cat=5
cats=[cat, 'Anakin', 'God Father', 6]

# [start_index:stop_index]
print(cats[1:2])
# [start_index:stop_index:step]
print(cats[1:4:2])


immutable_cats = tuple(cats) # cast la tipul tuple
print(immutable_cats)
# Tuples: (), este o lista, e immutable (nemodificabila)
cats = (cat, 'Anakin', 'God Father', 6, 9)
print(cats[2:3])

# Dictionaries: { key: value, key2: value2}; key - immutable values (strings, tuples, int, float)
laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    6: 9,
    #cats: 67,
    #"dictionary": {
        #cats: 56
    #}
}
print(laptops)
apple_ram = laptops["Apple"]
print(apple_ram)
#cats_value = laptops[cats]

laptops.update({"new value": "from update method"})

print(laptops)
#dictionary = laptops["dictionary"][cats]

print(json.dumps(laptops, indent=4))
print()
print(laptops.values())
print(laptops.keys())
