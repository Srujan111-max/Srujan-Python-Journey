'''Variable-length arguments:
You can use *args and **kwargs to accept a variable number of arguments in a funtion'''

#1) Using of *args (args = arguments)
print("__________________________________________________")
print("1st o/p:")
def add(*a):
    print(a) #o/p: (12, 45, 678, 98)
    print(type(a)) #o/p: <class 'tuple'>
    print(sum(a))

print(add(12,45,678,98)) # This will return None but the function will do as it is programmed to work
print("__________________________________________________")

#2) But if we want dictionary then we use **kwargs (kwargs = key word arguments)
print("__________________________________________________")
print("2nd o/p:")
def student_info(**details): # Here **details is **kwargs
    for key,value in details.items():
        print(f"{key}:{value}")
    print(type(details)) #o/p: <class 'dict'>
  
student_info(Name="Srujan", age=19, course= "Python")
print(type(student_info)) #o/p: <class 'function'>
print("__________________________________________________")

#3) Recursion --> calling th one function within a same function (like 1 calling itself) 
print("__________________________________________________")
print("3rd o/p:")
def funtion1(num): # Here we r finding factorial without using loops
    if num == 1:
        return 1
    return num*funtion1(num-1)

print(f"Factorial  is: {funtion1(5)}") #o/p: Factorial  is: 120
print("__________________________________________________")

#4) Lambda funtions:
# --> this small function take any number of arguments but has onle one expression 
print("__________________________________________________")
print("4th o/p:")
# syntax --> lambda arguments: expression

'''Instead of writing function
   def add(a,b):
       return a+b 
we'll do as -->
'''
add = lambda a,b : a+b
print(add(2,3)) #o/p: 5

double = lambda x : 2*x
print(double(200)) #o/p: 400
print("__________________________________________________")

#5) Another use of Lambda functions:
print("__________________________________________________")
print("5th o/p:")

''' If i want to sort dictionary in ascending or descending order based on marks then...
( Multiple dictionaries are given in list format)... 
'''

students = [
    {"name":"srujan", "marks": 70},
    {"name":"sujay", "marks": 95},
    {"name":"sachin", "marks": 50}
]
 
students.sort(key= lambda x: x["marks"])
print(students) # Ascending order
students.sort(key= lambda x: x["marks"], reverse = True)
print(students) # Descending order
print("__________________________________________________")

#6)
print("__________________________________________________")
print("6th o/p:")
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5),"--> factorial of 5")
print("__________________________________________________")

#7) Nested functions: 
print("__________________________________________________")
print("7th o/p:")
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("Srujan")
print("__________________________________________________")

#8)
print("__________________________________________________") 
print("8th O/p:".casefold())
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
print("__________________________________________________")