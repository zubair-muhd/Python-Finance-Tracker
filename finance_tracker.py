import json
from datetime import datetime

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.filename = "transactions.json"
        self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as file:
                self.transactions = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.transactions = []

    def save_transactions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self):
        try:
            amount = float(input("Enter amount: "))
            type_ = input("Enter type (income/expense): ").lower()
            if type_ not in ['income', 'expense']:
                print("Invalid type! Must be 'income' or 'expense'.")
                return
            category = input("Enter category (e.g., Food, Salary): ").capitalize()
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            transaction = {
                "amount": amount,
                "type": type_,
                "category": category,
                "date": date
            }
            self.transactions.append(transaction)
            self.save_transactions()
            print("Transaction added successfully!")
        except ValueError:
            print("Invalid amount! Please enter a number.")

    def view_summary(self):
        if not self.transactions:
            print("No transactions available.")
            return

        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = total_income - total_expense

        print("\nFinancial Summary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Balance: ${balance:.2f}")

    def view_by_category(self):
        if not self.transactions:
            print("No transactions available.")
            return

        categories = {}
        for t in self.transactions:
            category = t["category"]
            if category not in categories:
                categories[category] = {"income": 0, "expense": 0}
            categories[category][t["type"]] += t["amount"]

        print("\nTransactions by Category:")
        for category, totals in categories.items():
            print(f"{category}:")
            print(f"  Income: ${totals['income']:.2f}")
            print(f"  Expenses: ${totals['expense']:.2f}")

    def view_all_transactions(self):
        if not self.transactions:
            print("No transactions available.")
            return

        print("\nAll Transactions:")
        for i, t in enumerate(self.transactions, 1):
            print(f"{i}. {t['date']} - {t['type'].capitalize()}: ${t['amount']:.2f} ({t['category']})")

def main():
    tracker = FinanceTracker()
    while True:
        print("\nPersonal Finance Tracker Menu:")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View Transactions by Category")
        print("4. View All Transactions")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_transaction()
        elif choice == "2":
            tracker.view_summary()
        elif choice == "3":
            tracker.view_by_category()
        elif choice == "4":
            tracker.view_all_transactions()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()