people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age
sorted_by_age = sorted(people, key=lambda x: x["age"])
print(sorted_by_age)