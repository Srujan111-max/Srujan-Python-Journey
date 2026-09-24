# Set .discard(), .remove() & .pop()

# My method
N = int(input())
numbers = set(map(int,input().split()))
comm = int(input())
commands = []
for i in range(comm):
    commands.append(input().strip().lower().split())
    if commands[i][0] == "remove":
        num = int(commands[i][1])
        if num in numbers:
            numbers.remove(num)
    elif commands[i][0] == "discard":
        num = int(commands[i][1])
        numbers.discard(num)
    elif commands[i][0] == "pop":
        numbers.pop()

print(sum(numbers))

# For HackerRank

N = int(input())
numbers = set(map(int, input().split())) # No .lower() and .strip() becoz the hackerrank gives only small letters and in formatted way
comm = int(input())

for _ in range(comm):
    command = input().split()

    if command[0] == "remove":
        num = int(command[1])
        numbers.remove(num)

    elif command[0] == "discard":
        num = int(command[1])
        numbers.discard(num)

    elif command[0] == "pop":
        numbers.pop()

print(sum(numbers))
