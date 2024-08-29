# Map (similar to JavaScript's map):

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 35}
]

names = list(map(lambda person: person["name"],people))
print(names)