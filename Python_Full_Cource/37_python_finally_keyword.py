try:
    # Code that might raise an exception
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
    print(f"10 divided by {user_input} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print(f"Thank you for using the calculator.")
    

def get_user_input():
    while True:
        try:
            user_input = int(input("Enter a positive number: "))
            if user_input <= 0:
                raise ValueError("Number must be positive")
            return user_input
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        finally:
            print("Input attempt completed!.")

def calculate_square_root(number):
    try:
        result = number ** 0.5
        print(f"The square root of {number} is {result:.2f}")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
    finally:
        print("Calculation completed!")
        
def main():
    try:
        user_input = get_user_input()
        calculate_square_root(user_input)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        print(f"Thank you for using the square root calculator.")

if __name__ == "__main__":
    main()
