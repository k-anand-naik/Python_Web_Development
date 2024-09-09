
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 35}
]

# Find (similar to JavaScript's find):

first_person_over_30 = next((person for person in people if(person["age"] > 80)),"Default value when not found")
print(first_person_over_30)

# Filter (similar to JavaScript's filter):

filtered_people_over_30 = list(filter(lambda person: person["age"]>30, people))
print(filtered_people_over_30)

# Map (similar to JavaScript's map):

names = list(map(lambda person: person["name"],people))
print(names)

# Reduce (similar to JavaScript's reduce):

from functools import reduce
# calculate the total age

total_age = reduce((lambda acc, person: acc+person["age"]),people,0)
print(total_age)



# ===========================================================================================

# 
from functools import reduce

transactions = [
    {"type":"income", "amount":100},
    {"type":"invest", "amount":130},
    {"type":"income", "amount":920},
    {"type":"expenditure", "amount":110}
]

def filtered_data(transactions):
    return filter(lambda t: t["type"] == "income", transactions)

def map_data(transactions):
    return map(lambda t: t["amount"], filtered_data(transactions))

def reduce_data(transactions):
    return reduce(
        lambda acc, amount: acc + amount,
        map_data(transactions),
        0
    )

total_amount = reduce_data(transactions)
print(f"total amount of income type is : {total_amount}")