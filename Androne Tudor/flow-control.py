from json import dumps

print(dumps(laptops, indent = 4))

print()

for key, value in laptops.items():
    print(key)
    print(value)

print()

for key in laptops.items():
    print(key)

print()

for value in laptops.values():
    print(value)

print("----------------")

for value in laptops.values():
    if type(value) is dict:
        print(dumps(value, indent = 4))
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