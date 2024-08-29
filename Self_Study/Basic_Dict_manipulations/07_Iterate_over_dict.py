person = {"name": "Alice", "age": 30, "city": "New York"}


# Iterate over the keys
print("printing keys")
for key in person:
    # print(f"Key: {key}, Value: {person[key]}")
    print(key)


# Iterate over the values
print("printing values")
for value in person.values():
    print(value)


# Iterate over the key-value pairs
print("printing key-value pairs")
for key, value in person.items():
    print(f"{key}: {value}")