# key value pair

from numpy import str0


customer = {
    "name": "John Smith",
    "email": "joe@gmail.com",
    "age": 30,
    "is_male": True
}

print(customer["name"])
customer["name"]  = "jack"
print(customer["name"])

digit_map = {
    "1":  "one",
    "2":  "two",
    "3":  "three",
    "4":  "four",
    "5":  "five",
    "6":  "six",
    "7":  "seven",
}

digit = "34271"
str2 = "";
for ch in digit:
    str2 += digit_map.get(ch) + " "

print(str2)
