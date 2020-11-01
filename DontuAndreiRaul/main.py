import json  # javascript objects

print('Hello world!')

cat = "Mic"
print(cat)

cat = 5
print(cat)

cats = [cat, "Anakin", 5, 6, 2, 7]
print(cats)

# [start_index:stop_index]
print(cats[1:2])
# [start_index:stop_index:step]
print(cats[1:5:3])

immutable_cats = tuple(cats) #cast la tipul tuple
print(immutable_cats)

# Tuples:(), este o lista, e immutable (nemodificabila)
cats = (cat, "Anakin", "God Father", 6, 9)
print(cats[2:3])
print(cats[1:4:2])
print(cats[3])

this_ide = "PyCharm"
print(tuple(this_ide))

# Dictionar: {key: value, key2:value2}; key - immutable values(string, tuple, int, float)
laptops = {
    "HP": "4 ram",
    "Apple":5,
    "DELL": 3,
    "Samsung":7,
    6: 9,
    "cats": ["56", 56],
    "dictionary":{
        "cats": 56,
        "pull": "request",
"another": {
    45: 555
}
    }

}
print(laptops)
apple_ran = laptops["Apple"]
print(apple_ran)
# cats_value = laptops[cats]
# print(cats_value)

dictionary = laptops["dictionary"].get("another").get(4)
print(dictionary)

laptops.update({"new value": "from update method"})
print(json. dumps(laptops, indent=4))
print()
print(laptops.values())
print(laptops.keys())
# a_tuple = ("abc", 'D')
# print(type(a_tuple))
# wannabe_tuple = (4, )
# print(wannabe_tuple)
