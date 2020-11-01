import json  # javascript object notation

print("Hello world!")

cat = 'Mickey'
print(cat)

cat = 5
print(cat)

cats = [cat, 'Anakin', 5, 6, 2, 7]
print(cats)

#  [start_index:stop_index]
print(cats[1:2])
#  [start_index:stop_index:step]
print(cats[1:5:3])

immutable_cats = tuple(cats)  # cast la tipul tuple
print(immutable_cats)
# Tuples: (), este o lista, e immutable (nemodificabila), se comporta ca o constanta
cats = (cat, 'Anakin', 'God Father', 6, 9)
print(cats[2:3])
print(cats[1:4:2])
print(cats[3])
this_ide = "PyCharm"
print(tuple(this_ide))

# Dictionaries: { key: value, key2: value2}; key - immutable values (strings, tuples, int, float)
laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    6: 9,
    "cats": ['56', 56],
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
print(dictionary)

laptops.update({"new value": "from update method"})
print(json.dumps(laptops, indent=4))
print()
print(laptops.values())
print(laptops.keys())
# a_tuple = ('abc', 'D')
# print(type(a_tuple))
# wannabe_tuple = (4,)
# print(wannabe_tuple)
