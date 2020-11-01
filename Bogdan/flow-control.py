"""
from json import dumps
laptops= {
    "HP": "4 ran",
    "Apple": 5,
    "DELL": 3,
    "Samsung": 4,
    111: [3,4,5]
}

for key, value in laptops.items():
    print(key)
    if type(value) is dict:
        print(dumps(value, indent=4))
        continue
    if type(value) is list:
        print(dumps(value, indent=4))
        for item in value:
            print(item)
"""

    count=0
    while count < 5:
        print(count)
        count+=1







