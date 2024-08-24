marks = [32,12,53,56,34,87,33]

# Without enumeration
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print(f"Right there!")
    index += 1


# with enumeration

for index, mark in enumerate(marks):
    print(f"Index: {index}, Mark: {mark}")
    if(index == 3):
        print(f"Right there at index {index}!") 