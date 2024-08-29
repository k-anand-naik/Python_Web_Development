def filter_transactions(filter_func, transactions):
    return [t for t in transactions if filter_func(t)]

is_income = lambda t: t["type"] == "income"



transactions = [
    {"type": "income", "amount": 100},
    {"type": "invest", "amount": 130},
    {"type": "income", "amount": 920},
    {"type": "expenditure", "amount": 110}
]

income_transactions = filter_transactions(is_income, transactions)
print(income_transactions)  # Output: [{"type": "income", "amount": 100}, {"type": "income", "amount": 920}]