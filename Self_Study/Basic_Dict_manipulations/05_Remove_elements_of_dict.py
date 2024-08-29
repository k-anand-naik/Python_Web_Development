person = {"name": "Alice", "age": 30, "city": "New York", "job": "Engineer"}

# Remove a specific item
del person["job"]

# Remove and return an item
age = person.pop("age")

# Remove and return the last inserted item
last_item = person.popitem()

print(person)  # Output: {'name': 'Alice'}
print(age)  # Output: 30
print(last_item)  # Output: ('city', 'New York')
last_item_dict = {last_item[0]:last_item[1]}

print(last_item_dict)

# =============================================================================================

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Using the pop() method
my_dict.pop('age')
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

# Using the del keyword
del my_dict['city']
print(my_dict)  # Output: {'name': 'John'}

# Using the popitem() method (removes the last inserted key-value pair)
my_dict.popitem()
print(my_dict)  # Output: {}

# Using the clear() method to remove all elements
my_dict.clear()
print(my_dict)  # Output: {}
