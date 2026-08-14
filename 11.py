print ("Taking List as input: ")

list1 = [num for num in input("Enter the list: ").split()] # split() function makes/separates the given appearance into list  
print (f"{list1} - these elements are separated and stored as strings") # here the inputs will be separated by split() and got stored as string in list

# to store it as integer then we do 
list1 = [int(num) for num in input("Enter the integers in the list: ").split()]
print(f"{list1} - these elements are separated and stored as integers")