# Example transactions list
transactions = [
    {"amount": 100, "type": "credit"},
    {"amount": 130, "type": "debit"},
    {"amount": 920, "type": "credit"},
    {"amount": 110, "type": "debit"},
]

# Generator version
def amount_generator(transactions):
    for t in transactions:
        yield t["amount"]

# Normal version
def amount_list(transactions):
    amounts = []
    for t in transactions:
        amounts.append(t["amount"])
    return amounts

# Using the generator version
gen = amount_generator(transactions)
print("Using Generator:", list(gen))  # Output: [100, 130, 920, 110]

# Using the normal version
amounts = amount_list(transactions)
print("Using Normal Function:", amounts)  # Output: [100, 130, 920, 110]
