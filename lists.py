# comment section

names = ["John", "Mary", "Sam", "Tom"]

print(names)
print(names[2])
## strange !!!
print(names[-1])
print(names[0:2])

print("Numbers example")
num = [1, 3, 5, 6, 7, 9]

num.append(22)
num.insert(0, -1)

for item in num:
    print(item)

print("Length is: " + str(len(num)))

print("Range example")
for item in range(5):
    print(item)

print("Start from 2")
for item in range(2,10):
    print(item)

print("Print with seep of 2")
for item in range(2,10,2):
    print(item)

print("2D list")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)
    print()

#unpacking 
x,y,z = num[0:3]
print(y)