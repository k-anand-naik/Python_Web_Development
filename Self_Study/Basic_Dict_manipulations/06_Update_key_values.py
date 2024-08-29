person = {"name": "Alice", "age": 30}

# Changing a value
person["age"] = 31

# Using the update() method
person.update({"name": "Alicia", "age": 32})

print(person)  # Output: {'name': 'Alicia', 'age': 32}