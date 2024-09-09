#  Lambda Functions (Anonymous Functions)

transactions = [
    {"type": "income", "amount": 100},
    {"type": "invest", "amount": 130},
    {"type": "income", "amount": 920},
    {"type": "expenditure", "amount": 110}
]

get_amount = lambda t: t["amount"]
get_type = lambda t: t["type"]
print(f"Amount list : {list(map(get_amount, transactions))}")
print(f"Type list : {list(map(get_type, transactions))}")


income_transactions = list(filter(lambda t: t["type"] == "income", transactions))
print(f"Income Transactions: {income_transactions}")
