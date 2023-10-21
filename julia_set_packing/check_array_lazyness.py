
def double(a):
    print(a)
    return a*2

b = iter(double(a) for a in range(10))

a = [double(a) for a in range(10)]


print("lazy line")
print(list(b))
print(a)

