import json
from collections import defaultdict

transactions = [
    {"type": "income", "amount": 100, "date": "2023-01-01"},
    {"type": "invest", "amount": 130, "date": "2023-01-02"},
    {"type": "income", "amount": 920, "date": "2023-01-03"},
    {"type": "expenditure", "amount": 110, "date": "2023-01-04"},
    {"type": "income", "amount": 500, "date": "2023-01-05"},
    {"type": "invest", "amount": 200, "date": "2023-01-06"},
]


def group_and_sum(transactions):
    grouped_amount_dict = defaultdict(list)

    for transaction in transactions:
        grouped_amount_dict[transaction["type"]].append(transaction["amount"])
    
    print(f"Grouping transaction of amount type {grouped_amount_dict}")

    result = {
        transaction_type: {
            "total_amount": sum(amounts),
            "transaction_count": len(amounts),
            "transaction_average": sum(amounts) / len(amounts)
        }   
        for transaction_type, amounts in grouped_amount_dict.items()
    }

    return {
        "data": result
    }

result = group_and_sum(transactions)
print(json.dumps(result, indent=2))