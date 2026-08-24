def mutate(w,p,c):
    list1 = list(w)
    print(list1)
    list1[p] = c
    w = "".join(list1)
    return w 

word = input("Enter the word: ")
pos = int(input("Enter the position: "))
char = input("Enter the letter: ")

result = mutate(word,pos,char)
print(result)