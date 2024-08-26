print("Select options: ")
print("1. Addition.")
print("2. Multiplication.")
print("3. Division.")
print("4. Subtraction.")
print("5. Modulo.")
print("6. Floor Division.")

option = int(input("Enter an option (1/2/3/4/5/6): "))
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

# Using if-else to perform the operation
if option == 1:
    result = num1 + num2
elif option == 2:
    result = num1 * num2
elif option == 3:
    if num2 != 0:
        result = num1 / num2
    else:
        result = f"Division with {int(num2)} is not allowed"
elif option == 4:
    result = num1 - num2
elif option == 5:
    if num2 != 0:
        result = num1 % num2
    else:
        result = f"Modulo by {int(num2)} is not allowed"
elif option == 6:
    if num2 != 0:
        result = num1 // num2
    else:
        result = f"Floor Division with {int(num2)} is not allowed"
else:
    result = "Invalid Option"

print("Result is:", result)