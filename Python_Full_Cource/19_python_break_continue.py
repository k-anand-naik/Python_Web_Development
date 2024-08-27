# # Continue statement skips the iteration when condition matches.
# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)
  
  
  
# Break statement = break the entire loop when the condition satisfies
i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break