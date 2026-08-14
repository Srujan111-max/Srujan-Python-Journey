l = [1,2,3,4,5,575]
dl = []
for num in l:
    dl.append(num)
    print(dl)

dict1 = {"srujan" : 95, "name2" : 85, 'name3' : 75}
for names in dict1:
    print (names)
for names in dict1.items():
    print (names)
print (dict1)
for names in dict1.keys():
    print (names)
print (dict1)
for names in dict1.values():
    print (names)
print (dict1)

ict1 = {"srujan" : 95, "name2" : 85, 'name3' : 75}
for names,marks in dict1.items():
    print (f"{names} - {marks}")