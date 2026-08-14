name = input ("Enter: ").lower()
for hi ,letters in enumerate(name):
    print(letters*(hi+1))
for letters in enumerate(name):
    print(f"{letters} - INDEX")
for index ,letters in enumerate(name):
    print(f"{letters} is in {index+1} position")