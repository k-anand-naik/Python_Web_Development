# Manipulating Tuples (convert the tuple to list and then manipulate and then convert the list to tuple)

countries_1 = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries_1) # converting tuple to list
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries_1 = tuple(temp)
print(countries_1)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


# Tuple methods
# t.count(element) --> returns the count/frequency of an element in a tuple
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res_1 = tuple1.count(3)
print('Count of 3 in Tuple1 is:', res_1)

# t.index(element, start, end) --> returns the index of an element in a tuple
res_2 = tuple1.index(3)
res_3 = tuple1.index(3,4,8)
print('First occurrence of 3 is', res_2)
print('First occurrence of 3 is', res_3)

print(f"length of tuple1: {len(tuple1)}")

