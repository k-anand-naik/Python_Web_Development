marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)

# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# Syntax:
    # List = [Expression(item) for item in iterable if Condition]

    # Expression: It is the item which is being iterated.

    # Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

    # Condition: Condition checks if the item should be added to the new list or not.

lst = [i for i in range(45) if(i%2==0)]
print(lst)

# Example 1: Accepts items with the small letter “o” in the new list

list_data = ["naik","anand","k","venky"]

new_list = [i for i in list_data if "a" in i]
print(new_list)


# Example 2: Accepts items which have more than 4 letters
new_list_1 = [name for name in list_data if (len(name)>4)]
print(new_list_1)

# Check whether an item in present in the list?

if "naik" in new_list:
    print("Yes!, naik is present")
else:
    print("No! naik is not present")