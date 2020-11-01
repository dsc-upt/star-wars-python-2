import json

print(' Hello! ')

cat = 'Mickey'
print(cat)

cat = 5
print(cat)

cats = [cat, 'Anakin', 5, 6, 2, 7]
print(cats)


# [start-index, stop-index]
print(cats[1:2])
# [start-index, stop-index: step]
print(cats[1:5:3])

# cast la tipul tuple
immutable_cats = tuple(cats)
print('Immutable cats', immutable_cats)

# Tuples: (), este o lista, care este nemodificabila
cats = (cat, 'Anakin', 'Tobi')
print(cats)
print(cats[1:4:2])
print(cats[2])

this_ide = "PyCharm"
print(tuple(this_ide))

# Dictionaries: {key: value1, key: value2} ; key -immutable values

laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    "dictionary": {
        "cats": 56,
        'Pull': 'Request',
        "another": {
            45: 555
        }
    }
}
print(laptops)
apple_ram = laptops["Apple"]
print(apple_ram)
# cats_value = laptops[cats]
# print(cats_value)

dictionary = laptops["dictionary"].get("another").get(4)
print('Cats dictionary', dictionary)


laptops.update({"new value": "from update method"})

print()
print(laptops)
print(laptops.values())
print(laptops.keys())
#a_tupple = ('abc', 'D')
#print(type(a_tupple))
#wannabe_tuple = tuple("tuple")
#print(wannabe_tuple)


