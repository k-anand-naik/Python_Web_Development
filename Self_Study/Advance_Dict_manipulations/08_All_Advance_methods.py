from functools import reduce

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 35}
]

# Find
find_first_person_over_30 = next((person for person in people if(person["age"] > 80)),"Default value when not found")

# Filter
filtered_people_over_30 = list(filter(lambda person: person["age"]>30, people))

# Map
names = list(map(lambda person: person["name"],people))

# Reduce
total_age = reduce((lambda acc, person: acc+person["age"]),people,0)
