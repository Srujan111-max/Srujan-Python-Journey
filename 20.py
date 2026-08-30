distinct_heights = set()

number = int(input())
heights = list(map(int,input().split()))
for high in heights:
    distinct_heights.add(high)

summ = 0
for elements in distinct_heights:
    summ += elements

average = float(summ/len(distinct_heights))

print(f"{average:.3f}")
