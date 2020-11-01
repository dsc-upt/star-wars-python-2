import json #   javascript object notation

print("Hello world")

cat = 'Mickey'
print(cat)

cat = 5

cats = [cat, 'Anakin', 5, 6, 2, 7]
#   pot adauga obiecte noi cu cats.append
print(cats)

#   [start_index : stop_index] (si nu afiseaza ultimul index)
print(cats[1:2])

#   [start_index : stop_index : step]
print(cats[1:5:2])


#   Tuples: (), lista immutable (nemodificabila) -> se comporta ca o constanta
immutable_cats = tuple(cats)#  cast la tipul tuple
print(immutable_cats)
#   aici nu mai poti adauga cu .append

cats = (cat, 'Anakin', 'GodFather', 6, 9) #   declarat tuple direct fara cast
print(cats[2:3])
print(cats[1:4:2])
print(cats[3])

this_ide = "PyCharm"
print(tuple(this_ide))

#   Dictionaries: {key: value, key2: value2}; key - immutable values (strings, touples, int, float - doar valori nemodificabile)
laptops = {
    "HP": "budget",
    "Apple": "overpriced",
    "DELL": "kinda cool",
    "Samsung": 10,
    6: 9,
    cats: ['56', 56],
    "dictionary": {
        cats: 56,
        ('Merge', 'Pull'): 'Request', #     Touples tre sa aiba neaparat 2 iteme, dar daca totusi vrei unul singur, faci ('ceva',) adica nimic dupa virgula
        "another": {
        45: 555
        }
    }
}
print(laptops)
hows_apple = laptops["Apple"]
print(hows_apple)
cats_value = laptops[cats]
print(cats_value)

#   a_tuple = ('abc', '0')
#   print(type(a_tuple))
#   wannabe_tuple = (4,)
#   print(wannabe_tuple)

dictionary = laptops["dictionary"]["another"].get(45)
print(dictionary)

laptops.update({"new value": "from update method"})
print(laptops)
print(laptops.values())
print(laptops.keys())

print()
laptops = {
    "HP": "budget",
    "Apple": "overpriced",
    "DELL": "kinda cool",
    "Samsung": 10,
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
print(json.dumps(laptops, indent = 4))# afisare dictionare ca n json, indentate frumos
