a = 3
b = 2

def add(a,b):
    while b != 0:
        c = a&b
        a = a^b
        b = c << 1
    return int(a)

print(add(a,b))
