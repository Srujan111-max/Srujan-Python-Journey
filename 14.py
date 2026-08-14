#1)
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))

#2) Nested functions: 
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("Srujan")

#3) 
def calculate(a=20,b=3):
    def add():
        return (a+b)
    def sub():
        return (a-b)
    def mul():
        return (a*b)
    def div():
        return a/b
    return add(),mul(),sub()

print(calculate()) # it returns results in tuple 
print(type(calculate()))
    