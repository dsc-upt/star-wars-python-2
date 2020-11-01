import json
print ("Hello word")
cat = "Mickey"
print(cat)
cat = 5
print(cat)
cats = [cat, "Anakin", 5, 6, 7, 5, 6]
newcats = tuple(cats)
print(newcats)
print(cats)
print(cats[1:2])
print(cats[1:5:3])
print(cats[1])
this_ide = "Py Charm"
print(tuple(this_ide))
# Dictioanre
laptops = {
    "HP": "4Ram",
    "Apple": 5,
    "Dell": 3,
    "Samsung": 7,
    6: 9,
    18: "56",
    "dictionar": {
        13: 56,
         "Pull": "Request",
        "another": {
                45:555

        }
    }

}
print(laptops)
apple_ram = laptops["Apple"]
print(apple_ram)
cats_value = laptops[newcats]
print(cats_value)
dictionar = laptops["dictionar"].get("another").get(4)
print(dictionar)
laptops.update({"new value": "from update method"})
print(json.dumps(laptops, indent=4))