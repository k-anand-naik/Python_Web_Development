transactions = [
    {"type": "income", "amount": 100},
    {"type": "invest", "amount": 130},
    {"type": "income", "amount": 920},
    {"type": "expenditure", "amount": 110}
]

def sum_income_type(transactions):
    sum = 0
    for transaction in transactions:
        if(transaction["type"] == "income"):
            sum = sum + transaction["amount"]

    return sum

sum_income = sum_income_type(transactions)
print(f"Total income from income type transactions: {sum_income}")