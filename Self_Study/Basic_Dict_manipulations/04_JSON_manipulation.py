import json

# Encoding Python Objects to JSON
person = {"name": "Alice", "age": 30}
json_string_1 = json.dumps(person)
print(json_string_1)  # Output: {"name": "Alice", "age": 30}
print(type(json_string_1))



# Decoding JSON Strings into Python Objects:
json_string_2 = '{"name": "Bob", "age": 25}'
python_object = json.loads(json_string_2)
print(python_object)  # Output: {'name': 'Bob', 'age': 25}
print(type(python_object))  