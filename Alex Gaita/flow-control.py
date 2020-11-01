laptops = {
    "HP": "4 ram",
    "Apple": 5,
    "Dell": 3,
    "Samsung": 7,
    6: 9,
    "cats": ['56', '321'],
    "dictionary": {
        'Pull': "Request",
        "another": {
            45: 555
        }
    }
}
print(laptops)
from json import dumps

print(dumps(laptops, indent=4))
for key, value in laptops.items():
    print(key)
    print(value)
for key in laptops.keys():
    print(key)

for value in laptops.values():
    if type(value) is dict:
        print(dumps(value, indent=4))
        continue
    if type(value) is list:
        for item in value:
            print(item)
        continue
    print(value)
count = 0

while count < 5:
    print(count)
    count += 1
