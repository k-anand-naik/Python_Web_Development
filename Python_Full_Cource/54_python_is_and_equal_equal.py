# In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.

a = "hello"
b = "hello"
print(a == b)  # True
print(a is b)  # True

# ==============================

a = 5
b = 5
print(a == b)  # True
print(a is b)  # True

