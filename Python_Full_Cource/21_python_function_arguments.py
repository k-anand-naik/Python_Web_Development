# Function to calculate the average of two numbers
def calculate_average(num1, num2=0, *args, precision=2):
    """
    num1: Required Argument (must be provided)
    num2: Default Argument (default is 0 if not provided)
    *args: Variable length Arguments (accepts additional numbers)
    precision: Keyword Argument (specifies the number of decimal places)
    """
    
    # Include all numbers in the calculation (num1, num2, and any additional numbers in args)
    total_sum = num1 + num2 + sum(args)
    
    # Calculate the total number of values to average
    count = 2 + len(args)
    
    # Calculate the average
    average = total_sum / count
    
    # Return the average rounded to the specified precision
    return round(average, precision)

# Example usage:

# Required Argument and Default Argument
result1 = calculate_average(10)
print("Average with default argument:", result1)

# Required Arguments and changing Default Argument
result2 = calculate_average(10, 20)
print("Average with provided arguments:", result2)

# Required Arguments, Default Argument, and Variable Length Arguments
result3 = calculate_average(10, 20, 30, 40)
print("Average with additional numbers:", result3)

# Using Keyword Argument to specify precision
result4 = calculate_average(10, 20, 30, precision=3)
print("Average with specified precision:", result4)



def greet(fname, lname, mname="John", *args, **kwargs):
    """
    fname: Required Argument
    lname: Required Argument
    mname: Default Argument (defaults to "John" if not provided)
    *args: Arbitrary Arguments (accepts any additional arguments)
    **kwargs: Keyword Arbitrary Arguments (accepts any additional keyword arguments)
    """
    
    # Construct the greeting message using provided and default arguments
    message = f"Hello, {fname} {mname} {lname}"

    # Add additional arbitrary arguments to the message, if any
    if args:
        message += " " + " ".join(args)

    # Add additional keyword arguments to the message, if any
    if kwargs:
        message += " (" + ", ".join(f"{key}: {value}" for key, value in kwargs.items()) + ")"

    # Return the constructed greeting message
    return message

# Example usage:

# 1. Required and Default Arguments
result1 = greet("Amy", "Watson")
print(result1)  # Output: Hello, Amy John Watson

# 2. Required, Default, and Keyword Arguments
result2 = greet(fname="Jade", lname="Wesker", mname="Peter")
print(result2)  # Output: Hello, Jade Peter Wesker

# 3. Required, Default, Keyword, and Arbitrary Arguments
result3 = greet("Tony", "Stark", "Howard", "Genius", "Billionaire")
print(result3)  # Output: Hello, Tony Howard Stark Genius Billionaire

# 4. All types of arguments including Keyword Arbitrary Arguments
result4 = greet("Steve", "Rogers", "Grant", "Captain", title="Captain America", alias="Nomad")
print(result4)  # Output: Hello, Steve Grant Rogers Captain (title: Captain America, alias: Nomad)





# ==================================================

def name(**name):
    print(type(name))
    print(name) # name is a dictionary == {'mname': 'Anand', 'lname': 'Naik', 'fname': 'K'}
    print(f"Hello, {name["fname"]} {name["mname"]} {name["lname"]}")

name(mname = "Anand", lname = "Naik", fname = "K")