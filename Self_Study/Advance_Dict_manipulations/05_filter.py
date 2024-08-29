# Filter (similar to JavaScript's filter):

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 35}
]

filtered_people_over_30 = list(filter(lambda person: person["age"]>30, people))
print(filtered_people_over_30)