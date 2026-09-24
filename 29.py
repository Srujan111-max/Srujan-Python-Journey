# Set .union() Operation

a = int(input())
set_a = set(map(int,input().split()))
b = int(input())
set_b = set(map(int,input().split()))

final_set = set_a.union(set_b)
print(final_set)
print(len(final_set))
