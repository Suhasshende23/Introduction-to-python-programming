# Creating a dictionary
student = {
    "name": "Suhas",
    "age": 21,
    "course": "Python",
    "marks": [85, 90, 92]  # list inside dictionary
}

# Accessing values
print(student["name"])       # Output: Suhas
print(student["marks"])      # Output: [85, 90, 92]
print(student["marks"][1])   # Output: 90

# Adding a new key-value pair
student["email"] = "suhas@example.com"
print(student)

# Updating an existing value
student["age"] = 22
print(student)

# Removing a key-value pair
del student["course"]
print(student)

# Iterating through dictionary
for key in student:
    print(key, ":", student[key])

# Using items() to get both key and value directly
for key, value in student.items():
    print(f"{key} --> {value}")


# List of dictionaries
students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Luna", "house": "Ravenclaw", "patronus": None}
]


for student in students:
    print(f"Name: {student['name']}, House: {student['house']}")
