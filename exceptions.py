# exeptions handling 

try:
    age = int(input("What is your age?: "))
    print(age)
    x = 7
    y = 7/0
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("zero division")