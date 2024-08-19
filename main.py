from database import Database
from user import User
from transaction import Transaction
from report import Report
from budget import Budget
import getpass
from prettytable import PrettyTable
from datetime import datetime

def print_title():
    print("""
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║        Personal Finance Manager               ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """)

def main():
    db = Database()
    user_manager = User(db)
    transaction_manager = Transaction(db)
    report_manager = Report(db)
    budget_manager = Budget(db)

    while True:
        print_title()
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            if user_manager.register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists.")

        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            if user_manager.login(username, password):
                print("Login successful!")
                logged_in_menu(db, username)
            else:
                print("Invalid credentials.")

        elif choice == '3':
            print("Thank you for using Personal Finance Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    db.close()

def logged_in_menu(db, username):
    transaction_manager = Transaction(db)
    report_manager = Report(db)
    budget_manager = Budget(db)

    while True:
        print_title()
        print(f"Welcome, {username}!")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Monthly Report")
        print("4. Generate Yearly Report")
        print("5. Set Budget")
        print("6. Check Budget")
        print("7. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction(transaction_manager, username)
        elif choice == '2':
            view_transactions(transaction_manager, username)
        elif choice == '3':
            generate_monthly_report(report_manager, username)
        elif choice == '4':
            generate_yearly_report(report_manager, username)
        elif choice == '5':
            set_budget(budget_manager, username)
        elif choice == '6':
            check_budget(budget_manager, username)
        elif choice == '7':
            print("Logging out. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_transaction(transaction_manager, username):
    while True:
        type = input("Enter transaction type (income/expense): ").lower()
        if type in ['income', 'expense']:
            break
        print("Invalid transaction type. Please enter 'income' or 'expense'.")

    if type == "income":
        categories = ["Salary", "Freelance", "Investments", "Rental income", "Gifts received", "Refunds", "Other income"]
    else:
        categories = ["Housing", "Utilities", "Groceries", "Dining out", "Transportation", "Healthcare", "Insurance",
                      "Personal care", "Clothing", "Entertainment", "Education", "Travel", "Gifts given", "Debt payments",
                      "Savings/Investments", "Taxes", "Home maintenance", "Pet expenses", "Childcare", "Miscellaneous"]

    print("Available categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    while True:
        category_choice = input("Enter category number (or 'c' for custom category): ")
        if category_choice.lower() == 'c':
            category = input("Enter custom category: ")
            break
        elif category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            category = categories[int(category_choice) - 1]
            break
        else:
            print("Invalid choice. Please try again.")

    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    
    transaction_manager.add_transaction(username, type, category, amount, date)
    print("Transaction added successfully!")

def view_transactions(transaction_manager, username):
    transactions = transaction_manager.get_transactions(username)
    if not transactions:
        print("No transactions found.")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Type", "Category", "Amount", "Date"]
    for t in transactions:
        table.add_row([t[0], t[2], t[3], f"${t[4]:.2f}", t[5]])
    
    print(table)

def generate_monthly_report(report_manager, username):
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    report = report_manager.generate_monthly_report(username, year, month)
    
    table = PrettyTable()
    table.field_names = ["Category", "Amount"]
    table.add_row(["Income", f"${report['income']:.2f}"])
    table.add_row(["Expenses", f"${report['expenses']:.2f}"])
    table.add_row(["Savings", f"${report['savings']:.2f}"])
    
    print(f"\nMonthly Report for {datetime(year, month, 1).strftime('%B %Y')}:")
    print(table)

def generate_yearly_report(report_manager, username):
    year = int(input("Enter year: "))
    report = report_manager.generate_yearly_report(username, year)
    
    table = PrettyTable()
    table.field_names = ["Category", "Amount"]
    table.add_row(["Income", f"${report['income']:.2f}"])
    table.add_row(["Expenses", f"${report['expenses']:.2f}"])
    table.add_row(["Savings", f"${report['savings']:.2f}"])
    
    print(f"\nYearly Report for {year}:")
    print(table)

def set_budget(budget_manager, username):
    category = input("Enter budget category: ")
    amount = float(input("Enter budget amount: "))
    budget_manager.set_budget(username, category, amount)
    print("Budget set successfully!")

def check_budget(budget_manager, username):
    category = input("Enter category to check: ")
    amount = float(input("Enter amount to check: "))
    if budget_manager.check_budget(username, category, amount):
        print("Warning: This transaction will exceed your budget!")
    else:
        print("Transaction is within budget.")

if __name__ == "__main__":
    main()