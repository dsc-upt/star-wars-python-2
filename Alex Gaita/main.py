import json

print("Hello World")

cat = 'Mickey'
print(cat)

cat = 5
print(cat)

cats = [cat, 'Anakin', 5, 6, 2, 7]
print(cats)

print(cats[1:2])
print(cats[::-1])

immutable_cats = tuple(cats)  # cast la tipul tuple
print(immutable_cats)
# Tuples:(),lista nemodificabila
cats = (cat, 'Anakin', 'God Father', 6, 9)

print(cats[2:3])
print(cats[1:4:2])
print(cats[3])

this_ide = 'PyCharm'
print(tuple(this_ide))

# Dictionaries:{}
laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "Dell": 3,
    "Samsung": 7,
    6: 9,

    "dictionary": {
        'Pull': "Request",
        "another": {
            45: 555
            }
        }
    }
print(laptops)
apple_ram = laptops['Apple']
print(apple_ram)
# print(laptops[cats])
dictionary = laptops['dictionary'].get("another").get(45)
print(dictionary)

laptops.update({"new_value": "from update method"})
print(json.dumps(laptops,indent=4))
