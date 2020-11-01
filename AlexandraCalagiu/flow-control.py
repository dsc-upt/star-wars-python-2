laptops = {
    "HP": "4 ram",
    "Apple": 3,
    "Dell": 5,
    "Samsung": 7,
    6: 9,
    "cats": ['56', 56],
    "dictionary": {
        "cats": 56,
        'Pull': "Request",
        "another": {
            45, '45'
        }
    }
}
"""from json import dumps
for item in laptops.items():
    print(item)
    print(item[0])
    print(item[1])
print("-----")
for value in laptops.values():
   if(type(value)) is dict:
       print(dumps(value, indent=4))
       continue

   if (type(value)) is list:
    for item in value:
       print(item)
    continue
print(value)"""
count = 0
while count < 5:
    print(count)
    count += 1
