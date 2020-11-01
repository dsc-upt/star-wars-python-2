import json

cats = [4, "ceva", 5, 6, 7, 8, 9]
cats = tuple(cats)

this_ide = "PyCharm"
print(tuple(this_ide))

laptops = {
    "HP": "4 RAM",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    # cats: ['56', 57],
    "dictionary":
        {
           "ion": 56,
           # ("Merge", 'Pull'): "Request"
        }
}
# apple_ram = laptops["Apple"]
# print(apple_ram)
# cats_value = laptops[cats]
# print(cats_value)

laptops.update({"new value": "from update method"})
print(json.dumps(laptops, indent=4))
print(laptops.values())
print(laptops.keys())

#
# dictionary = laptops("dictionary").get(cats)
# print(dictionary)
#
# wanna_tuple= tuple(3,)
# print(wanna_tuple)
