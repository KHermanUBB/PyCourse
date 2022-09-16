# function with no parameters
def greet_usera():
    print("hello all")

# parameters passing 
def greet_userb(name):
    print(f"hello {name}")

def square(num):
    return num*num

print("start")
greet_usera()
greet_userb("john")
print(square(5))
print("stop")

