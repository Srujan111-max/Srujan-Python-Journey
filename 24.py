# String formatting

# Method 1
number = int(input("Enter number: "))
width = len(bin(number)[2:])

for i in range(1, number + 1):
    print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:]:>{width}} {bin(i)[2:]:>{width}}")

# Method 2
width = len(bin(number)[2:])

for i in range(1, number + 1):
    print(
        f"{i:>{width}} "
        f"{oct(i)[2:]:>{width}} "
        f"{hex(i)[2:]:>{width}} "
        f"{bin(i)[2:]:>{width}}"
    )

# Method 3
width = len(bin(number)[2:])

for i in range(1, number + 1):
    print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")