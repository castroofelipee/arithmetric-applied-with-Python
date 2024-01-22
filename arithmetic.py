class FinancialCalculator: 
    def __init__(self):
        self.balance = 0
        
    def add_income(self, amount):
        self.balance += amount
        print(f"Income of ${amount} added. New balance: ${self.balance}")
        
    def add_expense(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Expense of ${amount} deducted. New balanc: ${self.balance}")
        else:
            print("Insufficient funds. Expense cannot be added.")
            
            
        def check_balance(self):
            print(f"Current Balance: ${self.balance}")
            

def main():
    calculator = FinancialCalculator()
    
    while True:
        print("\n--- Financial Calculator ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            income = float(input("Enter income amount: "))
            calculator.add_income(income)
            
        elif choice == '2':
            exepense = float(input("Enter expense amount: "))
            calculator.add_expense(exepense)
            
        elif choice == '3':
            calculator.check_balance()
            
        elif choice == '4':
            print("Existing the Financial Calculator. Goodbye!")
            
        else:
            print("invalid choice. Please enter a number between 1 and 4.")
            
if __name__ == "__main__":
    main()