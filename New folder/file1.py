import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print('Hello world')

var1 = "hello"
var2 = 500
var3 = 22.5
var4 = 1j
var5 = ["rre", "dsa"]
var6 = ("red", "green")
# var7 =

print(type(var6))


one = int(input("Enter a value: "))
if one > 80:
    print("A")
elif 80 > one > 50:
    print("B")
else:
    print("F")

myList = [1, 2, 3, 4, 5]
Sum = 0
for x in myList:
    Sum += x
print(Sum)

Sum = 0
for x in range(1, 10, 1):
    Sum += x
print(Sum)


def list_para(newlist):
    answer = 0
    for x in newlist:
        answer += x
    return answer


if list_para([10, 20, 30, 40, 50, 60]) > 100:
    print("big")
else:
    print("small")

first = "Hello"[::-1]
last = "World"[::-1]
txt = first + " " + last
print(txt)
