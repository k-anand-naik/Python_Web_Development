l = [11, 45, 1, 2, 4, 6, 1, 1]

# append adds elements at end
l.append(122)

sorted_l = sorted(l)
print(f"Original list: {l}")
print(f"Sorted new list: {sorted_l}")
l.sort()
print(f"Original list after deep sorted: {l}")

# Reverse list
l.reverse()
print(l)

# index of a perticular element 
print(l.index(1))

# count the number of times an element appears
print(f"count of 1 in the list : {l.count(1)}")

# copy an array/list (don't do new_copy = l, it will point the same list in the memory)
new_copy = l.copy()
new_copy[2] = 123
print(f"copied list: {new_copy}")


# insert
list_color = ["red","black","blue"]
list_color.insert(1, "yellow") # add new element called "yellow" at index 1
print(list_color)

# extend method of list
m = [1234,1211,1113]
l.extend(m)
print(l)

# Concatenate
k = l + m
print(k)