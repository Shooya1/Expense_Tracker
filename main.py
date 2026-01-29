from datetime import date
from storage import load_expenses, save_expenses
from reports import total_expenses, expenses_by_category

expenses = load_expenses()

def generate_id():
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1

def add_expense():
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Invalid amount.")
    
    category = input("Category: ")
    description = input("Description: ")

    expense = {
        "id": generate_id(),
        "amount": amount,
        "category": category,
        "description": description,
        "date": str(date.today())
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for e in expenses:
        print(
            f'{e["id"]} | {e["date"]} | '
            f'{e["category"]} | '
            f'{e["description"]} | '
            f'{e["amount"]}'
        )

def show_reports():
    print("\nReports")
    print("1. Total expenses")
    print("2. Expenses by category")

    choice = input("Choose: ")

    if choice == "1":
        print(f"Total: {total_expenses(expenses)}")
    elif choice == "2":
        summary = expenses_by_category(expenses)
        for category, total in summary.items():
            print(f"{category}: {total}")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Reports")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_reports()
    
    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("Invalid Choice.")