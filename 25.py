# Alphabet rangoli

import string

size = int(input())
alphabet = string.ascii_lowercase
width = 4 * size - 3

for i in range(size - 1, -size, -1):
    row = alphabet[size - 1:abs(i):-1] + alphabet[abs(i):size]
    row = "-".join(row)
    print(row.center(width, "-"))
