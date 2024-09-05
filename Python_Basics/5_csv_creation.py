import pandas as pd

# Define the file name
file_name = 'user_details.xlsx'

# Initialize an empty list to store user data
user_data = []

while True:
    # Get user inputs
    user_name = input("Enter user name (or -1 to exit): ")
    if user_name == '-1':
        break
    
    user_company = input("Enter user company: ")
    user_experience = input("Enter user experience (in number of years): ")
    user_designation = input("Enter user designation: ")
    user_working_hours = input("Enter user working hours: ")
    
    # Append user details to the list
    user_data.append([user_name, user_company, user_experience, user_designation, user_working_hours])

# Convert list to DataFrame
df = pd.DataFrame(user_data, columns=['User Name', 'User Company', 'User Experience (Years)', 'User Designation', 'User Working Hours'])

# Save to Excel file (append if file exists)
try:
    with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, index=False, header=writer.sheets['Sheet1'].max_row == 0)
except FileNotFoundError:
    df.to_excel(file_name, index=False)

print(f"User details have been saved to {file_name}")
