def my_gen():
    n = 1
    print("This printed first")

    yield n

    n += 1
    print("This printed second")

    yield n

    n += 2
    print("This printed third")

    yield n

def rev_str(string):
    length = len(string)
    for i in range(length - 1,-1,-1):
        yield string[i]

##for char in rev_str("Hello"):
  ##  print(char)

my_list = [2,3,4,5]
#print([x**2 for x in my_list])
a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
