# To find out second lowest scorer names (it may be multiple names and there names are printing in alphabetical order)
list1 = []
set1 = set()
for i in range(int(input())):
    name = input()
    score = float(input())
    list1.append([name,score])
    set1.add(score)

second_low_score = sorted(set1)[1]
second_low_names = []

for names,scores in list1:
    if scores == second_low_score:
        second_low_names.append(names)
print(second_low_names)

for name in sorted(second_low_names):
    print(name)