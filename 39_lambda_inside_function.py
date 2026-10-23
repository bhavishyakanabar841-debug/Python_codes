def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

num = int(input("Enter a number: "))

print("Double:", double(num))
print("Triple:", triple(num))
