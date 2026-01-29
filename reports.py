def total_expenses(expenses):
    return sum(expense["amount"] for expense in expenses)

def expenses_by_category(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    return summary