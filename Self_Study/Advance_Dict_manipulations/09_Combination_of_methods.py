# let transactions = [
#     {"type": "income", "amount": 100},
#     {"type": "invest", "amount": 130},
#     {"type": "income", "amount": 900},
#     {"type": "expandeture", "amount": 110}
# ];

# // Get total income
# let totalIncome = transactions
#     .filter(t => t.type === "income")
#     .map(t => t.amount)
#     .reduce((acc, amount) => acc + amount, 0);

# console.log(totalIncome); // Output: 1000


from functools import reduce

transactions = [
    {"type": "income", "amount": 100},
    {"type": "invest", "amount": 130},
    {"type": "income", "amount": 900},
    {"type": "expandeture", "amount": 110}
]

# Get total income
# total_income = reduce(
#     function,
#     list,
#     initial_value
# )
total_income = reduce(
    lambda acc, amount: acc + amount,
    map(lambda t: t["amount"], filter(lambda t: t["type"] == "income", transactions)),
    0
)

print(f"Total amount of income type is : {total_income}") # Output: 1000





# Explanation:

#     1. Filter (function, iterable) --> retunrs a iterable:
#     filter(lambda t: t["type"] == "income", transactions) filters out the transactions that are of type "income".
    
#     2. Map (function, iterable) --> retunrs a iterable:
#     map(lambda t: t["amount"], ...) maps the filtered transactions to their "amount" values.
    
#     3. Reduce (function, iterable, initial_value) --> returns a single accumulated value:
#     reduce(lambda acc, amount: acc + amount, ..., 0) then sums up the amounts starting with an initial accumulator value of 0.




from functools import reduce

transactions = [
    {"type":"income", "amount":100},
    {"type":"invest", "amount":130},
    {"type":"income", "amount":920},
    {"type":"expandeture", "amount":110}
]

def filtered_data(transactions):
    return filter(lambda t: t["type"] == "income", transactions)

def map_data(transactions):
    return map(lambda t: t["amount"], filtered_data(transactions))

def reduce_data(transactions):
    return reduce(
        lambda acc, amount: acc + amount,
        map_data(transactions),
        0
    )

total_amount = reduce_data(transactions)
print(f"total amount of income type is : {total_amount}")