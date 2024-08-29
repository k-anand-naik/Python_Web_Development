# Closures
# Closures are functions that capture the local variables from their enclosing scope. They can "remember" these variables even when the outer function has finished executing.

def make_adder(x):
    def adder(y):
        return x + y
    return adder

add_100 = make_adder(100)
print(add_100(50))  # Output: 150