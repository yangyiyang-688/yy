class FinancialRecord:
    def __init__(self):
        self.records = []

    def add_income(self, amount, description):
        record = {"type": "income", "amount": amount, "description": description}
        self.records.append(record)
        print(f"Income added: {amount} {description}")

    def add_expense(self, amount, description):
        record = {"type": "expense", "amount": amount, "description": description}
        self.records.append(record)
        print(f"Expense added: {amount} {description}")

    def get_balance(self):
        total_income = sum(record["amount"] for record in self.records if record["type"] == "income")
        total_expense = sum(record["amount"] for record in self.records if record["type"] == "expense")
        balance = total_income - total_expense
        return balance

    def display_records(self):
        print("Financial Records:")
        for record in self.records:
            type_label = "Income" if record["type"] == "income" else "Expense"
            print(f"  {type_label}: {record['amount']} {record['description']}")
        print(f"Balance: {self.get_balance()}")


def main():
    fin_record = FinancialRecord()

    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Records")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            fin_record.add_income(amount, description)
        elif choice == '2':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            fin_record.add_expense(amount, description)
        elif choice == '3':
            fin_record.display_records()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()