
# scripts.py
def square_of_numebrs(arr):
    result = list(map(lambda x: x**2, arr))
    return result

if __name__ == "__main__":
    print(f"Script file")



# importing_file.py


import script

# Define the array here
array_to_square = [1, 2, 3, 4]

# Call the function from the script module and pass the array
squared_numbers = script.square_of_numebrs(array_to_square)

# Print the result
print(squared_numbers)
