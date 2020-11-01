#from .datatypes import laptops

laptops = {
    "HP": "4 rami",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    6: 9,
    "cats": ['56', 56],
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
from json import dumps

print(dumps(laptops, indent=4))

for item in laptops.items():
    print(item[0])
    print(item[1])

for key, value in laptops.items():
    print(key)
    print(value)


for key in laptops.keys():
    print(key)

print("---------------------------")

for value in laptops.values():
    if type(value) is dict:
        print(dumps(value, indent=4))
        continue

    if type(value) is list:
        for item in value:
            print(item)
        #break
        continue
        # conteaza indentarea. daca era mai la dreapta, atunci continue era la for, asa e la if

    print(value)


count = 0
while count < 5:
    print(count)
    count += 1
