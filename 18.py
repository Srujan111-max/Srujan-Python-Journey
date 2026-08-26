

def wrap(string, max_width):
    final = ""
    for i in range(0, len(string), max_width):
        final += string[i : i+max_width] + "\n"
    return final

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)