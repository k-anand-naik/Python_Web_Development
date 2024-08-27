import time

# Get the current hour as an integer
current_hour = int(time.strftime('%H'))

# Print the current hour for debugging
print(f"Current hour: {current_hour}")

# Determine the appropriate greeting based on the current hour
if 5 <= current_hour < 12:
    greeting = "Good Morning"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

# Print the greeting
print(greeting)