import json
# java script

print("Hello world")

cat = "Mikey"
print(cat)

cats = [cat, 'Anakin', 5]
print(cats)

print(cats[1:2])
print(cats[1:5:3])

# Tuples: (), este o lista immutable
immutable_cats = (cat, 'Anakin', "God Father", 6, 9)
print(immutable_cats)

print(immutable_cats[2])
print(immutable_cats[0:3])

cats = tuple(cats) # converteste lista in tuple
print(cats)

this_ide = "PyCharm"
print(tuple(this_ide))

# Dictionaries: {key: value, key: value}; key - immutable values (string, tuples, int, float)
laptops = {
    "HP": "4 gb ram",
    "Apple": 6,
    "DELL": 3,
    "Samsung": 7,
    6: 9,
    "cats": ['a',65],
    "dictionary": {
        "cats": 56,
        "aa": 'Request',
        "another": {
            4: 'aa'
        }
    }
}
print(laptops)
# accesarea elementelor din dictionar: dictionar[key]
apple_ram = laptops["Apple"]
print(apple_ram)
cats_value = laptops["cats"]
print(cats_value)
print()
dictionary = laptops["dictionary"].get("another").get(4)
print(dictionary)

laptops.update({"new value": "from update method"}) # adauga o noua cheie in dictionar
print(laptops["new value"])

print(json.dumps(laptops, indent = 4)) # afisare dictionare cu json
print()
print(laptops.values())
print(laptops.keys())

