single_element_tuple_1 = (1) # not tuple
print(type(single_element_tuple_1))
single_element_tuple_2 = (1,) # yes tuple (dont mention when you are creating a single element tuple then add comma (,) at the end)
print(type(single_element_tuple_2))

tup = (1, 2, 76, 342, 32, "green", True)

# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

# Check for item:
if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
