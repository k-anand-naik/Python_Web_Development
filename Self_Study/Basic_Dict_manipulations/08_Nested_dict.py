employees = {
    "Alice": {"department": "HR", "salary": 60000},
    "Bob": {"department": "IT", "salary": 70000}
}

print(employees["Alice"]["department"])

employees["Charles"] = {"department": "DE", "salary":93333}

print(employees)

# from rich import print as rprint
# from rich.pretty import Pretty

# employees = {
#     "Alice": {"department": "HR", "salary": 60000},
#     "Bob": {"department": "IT", "salary": 70000},
#     "Charles": {"department": "DE", "salary": 93333}
# }

# # Pretty print the dictionary with rich
# rprint(Pretty(employees, indent_guides=True))


