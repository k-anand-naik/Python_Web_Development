a = "1"
# a = 1
b = "2"
# b = 2
# name = "Anand"
# surname = "naik"
# print(int(name) + int(surname)) # the string should be number to convert into a number. name can't be converted to number
print(a+b) # String concatenation
print(int(a) + int(b))

print(float(a)+float(b))

# Implicit TypeCasting
c = 1.9
d = 8

print(c + d)



# Two Types of Typecasting:


# Explicit Conversion (Explicit type casting in python)
    # The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.
    # It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)


# Implicit Conversion (Implicit type casting in python).
    # Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.
    # Python converts a smaller data type to a higher data type to prevent data loss.

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

