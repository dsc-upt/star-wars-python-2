import json # javascript object notation
print("Hello World!")
cat = "Daisy"
print(cat)

cat = 8
print(cat)

cats = [cat, "Luke", 5, 6, 2, 7]
print(cats)
print(cats[1:2])
print(cats[1:5:2])  # start_index:stop_index:step
immutable_cats = tuple(cats)  # cast at tuple type
print(immutable_cats)
# Tuples: () --> it's an immutable list; it's like a const
cats = (cat, 'Anakin', 'God Father', 6, 9)
print(cats)
print(cats[2:3])
print(cats[2])

this_IDE = "PyCharm"
print(tuple(this_IDE))

# Dictionaries: {key1:value1, key2:value2}; key=immutable values (string, tuple, int, float)
laptops = {
    "HP": "4 ram",
    "Apple": 3,
    "Dell": 5,
    "Samsung": 7,
    6: 9,
    "cats": ['56', 56],
    "dictionary": {
        cats: 56,
        'Pull': "Request",
        "another": {
            45, '45'
        }
    }
}
print(laptops)
apple_ram = laptops["Apple"]
print(apple_ram)
#cats_value = laptops[cats]

#print(cats_value)

# dictionary = laptops["dictionary"].get("another").get(2)
# print(dictionary)
laptops.update({"new value": "from update method"})

print(laptops)
print(laptops.values())
print(laptops.keys())
# print(json.dumps(laptops, indent=4))
"""a_tuple = ('abc', 'D')
print(type(a_tuple))
wannabe_tuple = tuple(5,)
print(wannabe_tuple)
"""

