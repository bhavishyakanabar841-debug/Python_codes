numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))
square = list(map(lambda x: x * x, even))

print("Original:", numbers)
print("Even numbers:", even)
print("Squares of even numbers:", square)
