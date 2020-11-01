laptops = {
    "HP": "4 gb ram",
    "Apple": 6,
    "DELL": 3,
    "Samsung": 7,
    6: 9,
    "cats": ['a', 65],
    "dictionary": {
        "cats": 56,
        "aa": 'Request',
        "another": {
            4: 'aa'
        }
    }
}

from json import dumps
print(dumps(laptops, indent=4))

print()

for key, value in laptops.items():
    print(key)
    print(value)

print("------------------------------")

for value in laptops.values():
    if type(value) is dict:
        print(dumps(value, indent=4))
        continue

    if type(value) is list:
        for item in value:
            print(item)
        continue

    print(value)

print("---------")
count = 2
while(count < 10):
    print(count)
    count += 2