# Partial functions are created using functools.partial, allowing you to fix a certain number of arguments of a function and generate a new function.

from functools import partial

transactions = [
    {"amount": 100, "type": "credit"},
    {"amount": 130, "type": "debit"},
    {"amount": 920, "type": "credit"},
    {"amount": 110, "type": "debit"},
]

# Partial Function for Income Filter

def filter_by_type(transactions, t_type):
    return [t for t in transactions if t["type"] == t_type]

filter_income = partial(filter_by_type, t_type="credit")
print(filter_income(transactions))
# Output: [{"type": "income", "amount": 100}, {"type": "income", "amount": 920}]
