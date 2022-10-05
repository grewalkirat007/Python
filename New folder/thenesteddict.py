family = {
    "Sib1": {
        "name": "Dave",
        "gender": "male",
        "birthYear": 1980
    },
    "Sib2": {
        "name": "Kate",
        "gender": "female",
        "birthYear": 1988
    },
    "Sib3": {
        "name": "Ed",
        "gender": "male",
        "birthYear": 1970
    },
}

# minimum = min(int(d['birthYear']) for d in family.values())
# print(minimum)

# by mee ###############
minimum = min(family.items(), key=lambda v: int(family[v[0]]['birthYear']))[1]['name']
print(minimum)


# by masterji ################# 
theyear = 2020
for x, y in family.items():
    # print x, y
    if(y["birthYear"] < theyear):
        theyear = y["birthYear"]
        name = y["name"]
print(name)

# for x,y in family.items():
#     print(x,y["name"])

# for x, y in family.items():
#     print(x, y["birthYear"])

# for x, y in family.items():
#     age = int(y["birthYear"])
#     if age <= max_age:
#         print(y["name"])

# mylist = [(int(family["Sib1"]["birthYear"])), (int(family["Sib2"]["birthYear"])), (int(family["Sib3"]["birthYear"]))]
# print(min(mylist))

# list_max = []
# list_name = []
# for x, y in family.items():
#     age = int(y["birthYear"])
#     name = y["name"]
#     list_max.append(age)
#     list_name.append(name)
# print(list_max)
# print(min(list_max))
# print(list_name)
# print(max(list_name))

# for y in family.values():
#     print(min(y["birthYear"]))
