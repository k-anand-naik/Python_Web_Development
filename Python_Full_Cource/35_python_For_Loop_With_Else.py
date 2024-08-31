print(f"\nWithout break statement")

for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Loop finished without breaking")
    
print(f"\nWithout break statement")

for i in range(6):
    print(i)
else:
    print("Loop finished without breaking")
    
# Key Difference:
# In the first snippet, the loop exits prematurely when i == 4, so the else block is skipped.
# In the second snippet, the loop completes its full iteration without any interruptions, so the else block is executed.