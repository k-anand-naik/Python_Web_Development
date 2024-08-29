import json
from datetime import datetime

transactions = [
    {"type": "income", "amount": 100, "date": "2023-01-01"},
    {"type": "invest", "amount": 130, "date": "2023-01-02"},
    {"type": "income", "amount": 920, "date": "2023-01-03"},
    {"type": "expenditure", "amount": 110, "date": "2023-01-04"},
    {"type": "income", "amount": 500, "date": "2023-01-05"},
    {"type": "invest", "amount": 200, "date": "2023-01-06"},
]

def transactions_in_date_range(transactions, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    return list(filter(
        lambda t: start <= datetime.strptime(t["date"], "%Y-%m-%d") <= end,
        transactions
    ))

start_date = "2023-01-02"
end_date = "2023-01-05"
filtered_transactions = transactions_in_date_range(transactions, start_date, end_date)
print(json.dumps(filtered_transactions, indent=2))

