print('Hello world!')

cat = "Mickey"
print(cat)

cat = 5
print(cat)

cats = [cat, "Anakin", 5, 6, 2 , 7]

print(cats)

# [start_index:stop_index]
print(cats[1:2])
# [start_index:stop_index:step]
print(cats[1:5:2])
immutable_cats = tuple(cats) #cast la tipul tuple
print(immutable_cats)
# Tuples : (), este o lista care e immutable (nemodificabila), se comporta ca o constanta
cats = (cat, 'Anakin', 'Tomi',6,9)
print (cats)
print(cats[2:3])
print(cats[1:4:2])
this_ide="PyCharm"
print (tuple (this_ide))

#Dictionaries : { key1:value , key2 : value2}; key = immutable values (strings , tuples , int, float)

laptops = {
    "HP" : "4 ram",
    "Apple" : 5,
    "DELL" : 3,
    "Samsung" : 7,
    cats : 67,
    "dictionary" : {
cats : 56,
        ('Merge', 'Pull') : 'Request'
    }
}
print(laptops)
apple_ram = laptops ["Apple"]
print(apple_ram)
cats_value = laptops[cats]
print(cats_value)