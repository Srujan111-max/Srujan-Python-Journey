N = int(input())
arr = []
for i in range(N):
    command = input().lower().strip().split()
    if command[0] == "insert":
        operation = "insert"
        position = int(command[1])
        integer = int(command[2])
        arr.insert(position,integer)                
    elif command[0] == "append":
        operation = "append"
        integer = int(command[1])
        arr.append(integer)
    elif command[0] == "remove":
        operation = "remove"
        integer = int(command[1])
        arr.remove(integer)
    elif command == "print":
        print(arr)
    elif command == "pop":
        arr.pop()
    elif command == "reverse":
        arr.reverse()

