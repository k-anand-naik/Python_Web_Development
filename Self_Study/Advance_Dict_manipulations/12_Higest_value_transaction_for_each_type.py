from operator import itemgetter
from collections import defaultdict
import json

transactions = [
    {"type": "income", "amount": 100, "date": "2023-01-01"},
    {"type": "invest", "amount": 130, "date": "2023-01-02"},
    {"type": "income", "amount": 920, "date": "2023-01-03"},
    {"type": "expenditure", "amount": 110, "date": "2023-01-04"},
    {"type": "income", "amount": 500, "date": "2023-01-05"},
    {"type": "invest", "amount": 200, "date": "2023-01-06"},
]


def highest_transactions(transactions):
    grouped_transaction = defaultdict(list)
    
    # Group transactions by type
    for transaction in transactions:
        grouped_transaction[transaction["type"]].append(transaction)
    
    print(json.dumps(grouped_transaction))
    
    
    # Create the response object
    response = {
        t_type: max(trans, key=itemgetter("amount"))
        for t_type, trans in grouped_transaction.items()
    }
    
    # Return the data encapsulated in an object with a "data" key
    return {
        "data": response
    }

# Get the highest transactions and print the JSON response
highest = highest_transactions(transactions)
print(json.dumps(highest, indent=2))
