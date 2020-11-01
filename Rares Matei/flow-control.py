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

from json import dumps

print(dumps(laptops, indent = 4))

for key, value in laptops.items() :
    print(key, value)

for value in laptops.values() :
    if type(value) is dict :
        print(dumps(value, indent = 4))
        continue # trece la urmatoarea iteratie

    if type(value) is list :
        for item in value:
            print(item)
        continue

    print(value)