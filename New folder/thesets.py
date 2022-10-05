set1 = {"red", "green", "blue"}
set2 = {1, 23, 24, 69}
set3 = {"red", "green", 25, 2.0, True, "white"}
set1.add("white")
set1.add("red")

print(set1)
print(set2)
print(set3)

for x in set1:
    print (x)

sum = 0
for x in set2:
    sum += x
print(sum)
