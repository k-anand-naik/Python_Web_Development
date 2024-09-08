import os

# #  Open the file in read-only mode
# f = os.open("read_text_file.txt", os.O_RDONLY)

# # Read the contents of the file

# content = os.read(f, 1024)
# print(content)

# # Close the file
# os.close(f)


# =================================================================
 
# # Writing to the file

# def delete_file(filename):
#     try:
#         os.remove(filename)
#         print(f"The file {filename} has been deleted successfully.")
#     except FileNotFoundError:
#         print(f"The file {filename} does not exist.")
#     except PermissionError:
#         print(f"You do not have permission to delete the file {filename}.")
#     except Exception as e:
#         print(f"An error occurred while trying to delete the file {filename}: {str(e)}")

# def write_to_file():
#     filename = "write_text_file.txt"

#     # # Check if the file exists, create it if not
#     # if not os.path.exists(filename):
#     #     f = os.open(filename, os.O_CREAT | os.O_WRONLY)
#     # else:
#     #     f = os.open(filename, os.O_APPEND | os.O_WRONLY)

#     # Using shorthand if-else condition to open the file
#     f = os.open(filename, os.O_CREAT | os.O_WRONLY) if not os.path.exists(filename) else os.open(filename, os.O_APPEND | os.O_WRONLY)

#     while True:
#         user_input = input("Enter a string (-1 to stop): ")
        
#         if user_input == "-1":
#             break
        
#         os.write(f, (user_input + "\n").encode())  # Convert the entire string to bytes
#         # os.lseek(f, 1, 1)  # Move cursor to next line

#     os.close(f)

# def main():
#     print("File Writer Menu:")
#     print("1. Write to file")
#     print("2. Delete file")
    
#     choice = input("Enter your choice (1/2): ")
    
#     if choice == "1":
#         write_to_file()
#     elif choice == "2":
#         filename = "write_text_file.txt"
#         delete_file(filename)
#     else:
#         print("Invalid choice.")

# if __name__ == "__main__":
#     main()

# =================================================================================================


