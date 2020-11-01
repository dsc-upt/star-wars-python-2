laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 7,

}
from json import dumps

print(dumps(laptops, indent=4))

for item in laptops.items():
    print(item[0], item[1])

for value in laptops.items():
    if type(value) is list:
        for item in value:
            print(item)

count = 0
while count < 5:
    print(count)
    count += 1
