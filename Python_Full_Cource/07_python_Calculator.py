print("Select options: ")
print("1. Addition.")
print("2. Multiplication.")
print("3. Division.")
print("4. Subtraction.")
print("5. Modulo.")
print("6. Floor Division.")

option = int(input("Enter a option (1/2/3/4/5/6): "))
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

# Create a dictionary to mimic the switch-case
result = {
    1: num1 + num2,
    2: num1 * num2,
    3: num1 / num2 if num2 != 0 else f"Division with {int(num2)} is not allowed",
    4: num1 - num2,
    5: num1 % num2 if num2 != 0 else f"Modulo by {int(num2)} is not allowed",
    6: num1 // num2 if num2 != 0 else f"Floor Division with {int(num2)} is not allowed"
}.get(option, "Invalid Option")

print("Result is :", result)

