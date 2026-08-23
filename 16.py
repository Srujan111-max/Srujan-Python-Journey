n = int(input("Enter the number of scorers/participants: "))

arr = map(int, input().split())
arr = set(arr)  # if given i/p is [2,3,6,6,5] then here to avoid 6 as second place we'll use set() so it becomes (2,3,6,5)
arr = list(arr) # Again we convert this to list so to sort that numbers
arr.sort()

print(arr[-2])