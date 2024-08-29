# Dictionary with initial key-value pairs
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 30
print(person.get("country", "Not specified"))  # Output: Not specified (default value)