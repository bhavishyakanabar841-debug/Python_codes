students = [
    ("Amit", 75),
    ("Riya", 90),
    ("Jay", 82)
]

topper = max(students, key=lambda x: x[1])
lowest = min(students, key=lambda x: x[1])

print("Highest marks:", topper)
print("Lowest marks:", lowest)
