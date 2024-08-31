# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# ======================================================================= 

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....

def fibonacci_recursive(n):
  """Calculates the nth Fibonacci number using recursion."""

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_series(n):
  """Prints the Fibonacci series up to the nth term using recursion."""

  for i in range(1, n + 1):
    print(fibonacci_recursive(i))

# Get the number of terms to print from the user
n = int(input("Enter the number of terms: "))

# Call the print_fibonacci_series function to print the series using recursion
print_fibonacci_series(n)
print(fibonacci_recursive.__doc__)

# =========================================================================

def fibonacci(n):
  """Prints the Fibonacci series up to the nth term."""

  if n <= 0:
    print("Please enter a positive integer.")
    return

  # Initialize the first two terms of the series
  fib_prev = 0
  fib_curr = 1

  # Print the first two terms
  print(fib_prev)
  print(fib_curr)

  # Generate and print the remaining terms
  for i in range(2, n):
    fib_next = fib_prev + fib_curr
    print(fib_next)

    # Update the previous and current terms for the next iteration
    fib_prev = fib_curr
    fib_curr = fib_next

# Get the number of terms to print from the user
n = int(input("Enter the number of terms: "))

# Call the fibonacci function to print the series
fibonacci(n)