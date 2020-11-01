import json #javascript object notation
print('Hello World!')
cat = 'Mickey'
print(cat)

cat = 5
print(cat)

cats = [cat, 'Anakin', 5, 6, 2, 7]
print(cats)

# [start_index:stop_index]
print(cats[1:2])
# [start_index:stop_index:step]
print(cats[1:5:2])

immutable_cats = tuple(cats) #cast la timpul tuple
print(immutable_cats)
# Tuples: (), este o lista, dar e immutable(nemodificabila), se comporta ca o constanta
cats = (cat, 'Anakin', 'Darboux', 6, 9)
print(cats[1:4:2])
# sunt salvate in memorie ca sa poata fi accesate cat mai usor. lista cere mai multa memorie pentru ca
# are mai multe proprietati
print(cats[3])

this_ide = "PyCharm"
print(tuple(this_ide))

# Dictionaries: { key: value, key2: value2}; key - immutable values ( strings, tuples, int, float)
# Dictionarele sunt cel mai smecher tip de data
# sunt ca JSON-urile
laptops = {
    "HP": "4 rami",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    6: 9,
   # cats: ['56', 56],
    "dictionary": {
        "cats": 56,
       # ('Merge', 'Pull'): 'Request',
        # tuples trebuie sa contina 2 elemente neaparat sau punem , si nimic (4,)
        "another_dictionary": {
            45: 555
        }

    }
   # [4, 5]: 44
}
print(laptops)

apple_ram = laptops["Apple"]
print(apple_ram)
#cats_value = laptops[cats]
#print(cats_value)

a_tuple = ('abc', 'D')
print(type(a_tuple))
#wannabe_tuple = tuple ('tuple')
wannabe_tuple = (4,)
print(wannabe_tuple)

#dictionary = laptops["dictionary"][cats]
#dictionary = laptops["dictionary"]["another_dictionary"][45]
dictionary = laptops["dictionary"].get("another_dictionary").get(4)
print(dictionary)

# ca sa adaugam o val noua la dictionar trebuie sa adaugam un alt dictionar
laptops.update({"new value": "from update method"})
print(json.dumps(laptops, indent = 4))
# lui json nu ii plac tuple-urile
print(laptops)
#print(laptops.values())
#print(laptops.keys())


