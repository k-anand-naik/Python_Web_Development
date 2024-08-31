# Without exception handling

a = input("Enter a number for multiplication table : ")

# for i in range(1, 11):
#     print(f"{int(a)} x {i} = {int(a) * i}")


# With exception handling

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a) * i}")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"Some important lines of code!")
print(f"code executed successfully")