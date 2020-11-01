import json #java script object notation

# tupples () -- lista nemodificabila, se comporta ca o constanta
cat = 5
cats = (cat, "anakin", "God Father", 7, 8)  # cast la tipul tupple
print(cats[3])

immutable_cats = tuple(cats)
print(immutable_cats)

#Dictionaries {key : value, key2 : value2}
#key - immutable value: strings, tupples, int, float

laptops = {
    "HP" : "4 ram",
    "Apple"  : 5,
    "Dell" : 3,
    "Samsung" : 7,
    'cats' : ['56', 56],
    "dictionary" : {
        'cats':56,
        'Pull': 'Request'
    }
}

print(type(laptops))
print(laptops)
apple_ram = laptops["Apple"]
print(apple_ram)

laptops.update({"new value": "from updated method"})
print(json.dumps(laptops))
print()
print(laptops.values())
print(laptops.keys())