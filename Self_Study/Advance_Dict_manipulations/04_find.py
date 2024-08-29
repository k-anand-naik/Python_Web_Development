people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 35}
]

# Find (similar to JavaScript's find):

first_person_over_30 = next((person for person in people if(person["age"] > 80)),"Default value when not found")
print(first_person_over_30)


# =================================================================



def find_transaction(transactions, condition, default=None):
    return next((t for t in transactions if condition(t)), default)

# Sample data
transactions = [
    {"id": 1, "type": "income", "amount": 100},
    {"id": 2, "type": "expense", "amount": 50},
    {"id": 3, "type": "income", "amount": 200},
    {"id": 4, "type": "expense", "amount": 75},
]

# Find the first income transaction over 150
result = find_transaction(
    transactions,
    lambda t: t["type"] == "income" and t["amount"] > 150,
    {"id": None, "type": "Not found", "amount": 0}
)

print(result)

# Find the first expense transaction over 100 (which doesn't exist)
not_found = find_transaction(
    transactions,
    lambda t: t["type"] == "expense" and t["amount"] > 100,
    {"id": None, "type": "Not found", "amount": 0}
)

print(not_found)