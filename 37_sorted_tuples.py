students = [
    ("Amit", 75),
    ("Riya", 90),
    ("Jay", 82)
]

result = sorted(students, key=lambda x: x[1])

print("Sorted by marks:")
for student in result:
    print(student)
