# LIST COMPREHENSION

# METHOD 1
l =[1,2,3,4]
dl = []
for num in l:
    dl.append(num*2)
print (dl)

# METHOD 2
A = [1,2,3,4]
B = [num**2 for num in A]
print(B)

# Here we dont need to take list1 i.e., A list so also instead we do
A = [a for a in range(1,5)] # A = [1,2,3,4]
B = [num*2 for num in A]
print(B)

# If i want only even numbers to be transferred in second list then...
A = [a for a in range (1,11)]
B = [num for num in A if num%2==0]
print(B)

# If i want to transfer the selective letters of string in list1 then...
A = ["srujan", "chandan", "chandrashekhar", "sachin", "sujay", "swamy", "Name n"]
B = [letter[0] for letter in A]
print(B)