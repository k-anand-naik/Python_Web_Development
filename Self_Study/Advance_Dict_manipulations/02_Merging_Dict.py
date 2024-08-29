# In Python 3.9+
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# For earlier Python versions
merged = {**dict1, **dict2}