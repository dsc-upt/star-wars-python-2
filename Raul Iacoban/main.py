import json

#print ("hello world")
"""
things= (1,2,3)
fixed_things = tuple(things)
fixed_things[1]=0
print(fixed_things)
"""

laptops = {
    "HP": "4 ram",
    "Apple": 1,
    "Dell": 2
}

laptops.update({"Lenovo": 3})
print(json.dumps(laptops, indent=1))

#print(laptops)