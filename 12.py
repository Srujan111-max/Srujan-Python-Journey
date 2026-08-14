def function1():
    print ("Hello! World")
function1()  

def function2(boy,girl): # boy and girl are parameters
    print (f"{boy} married {girl}")
function2("chandan", "chandana") # Positional arguments
function2(boy = "chandan", girl = "chandana") # Keyword arguments

def function3(boy,girl = "sadhana"): # Default parameters 
    print (f"{boy} married {girl}")
function3("srujan")

def function4(boy,girl = "sadhana"):
    print (f"{boy} married {girl}")
function4("srujan", "pooja hegde")

# RETURN IN FUNCTIONS
def function5 (num):
    return int(str(num)*3) #return we use when we want the value to used in further operation not to be printed

function5(5)
sum = 50 + function5(5)
print (sum)