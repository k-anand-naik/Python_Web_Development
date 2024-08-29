
# Decorators are functions that modify the behavior of another function. They are often used for logging, access control, or modifying input/output.

transactions = [
    {"amount": 100, "type": "credit"},
    {"amount": 130, "type": "debit"},
    {"amount": 920, "type": "credit"},
    {"amount": 110, "type": "debit"},
]

def log_transaction(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Logging Transaction: {result}")
        return result
    return wrapper

@log_transaction
def add_transaction(transactions, new_transaction):
    transactions.append(new_transaction)
    return new_transaction

new_transaction = {"type": "income", "amount": 500}
add_transaction(transactions, new_transaction)
