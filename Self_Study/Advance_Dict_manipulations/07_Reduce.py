# Reduce (similar to JavaScript's reduce):

from functools import reduce

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 35}
]

# calculate the total age

total_age = reduce((lambda acc, person: acc+person["age"]),people,0)
print(total_age)