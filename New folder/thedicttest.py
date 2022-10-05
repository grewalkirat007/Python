dict1 = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2016,
    "year": 2000,
    "isBrandNew": False,
    "colors": ["red", "grey", "white"],
}

dict2 = dict1.copy()

for x in dict1.keys():
    print(x)

for x in dict1.values():
    print(x)

for x,y in dict1.items():
    print(x, y)

print(dict1)
print(dict1["brand"])
print(dict1["colors"])
print(dict1.keys())
print(dict1.values())
