transactions = [
    {"amount": 100, "type": "credit"},
    {"amount": 130, "type": "debit"},
    {"amount": 920, "type": "credit"},
    {"amount": 110, "type": "debit"},
]


def calculate_total_income_recursive(transactions):
    if not transactions:
        return 0
    transaction = transactions[0]
    rest = transactions[1:]
    if transaction["type"] == "credit":
        return transaction["amount"] + calculate_total_income_recursive(rest)
    else:
        return calculate_total_income_recursive(rest)

total_income_recursive = calculate_total_income_recursive(transactions)
print(f"Total Income (Recursive): {total_income_recursive}")
