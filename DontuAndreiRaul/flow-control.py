
laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,
    6: 9,
    "cats": ["56", 56],
    "dictionary": {
        "cats": 56,
        "pull": "request",
        "another": {
                    45: 555
                    }
    }
}


from json import dumps

print(dumps(laptops, indent=4))

for key, value in laptops.items():
    print(key)
    print(value)

for key in laptops.keys():
    print(key)

print("__________________________")

for value in laptops.values():
    if type(value) is dict:
        print(dumps(value, indent=4))
        continue
    if type(value) is list:
        for item in value:
            print(item)
            break


print(value)

count = 0
while count < 5:
    print(count)
    count += 1
