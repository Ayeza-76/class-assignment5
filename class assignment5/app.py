class ATM:
    def __init__(self):
        # Initialize the ATM with default values
        self.balance = 1000.0
        self.pin = "1234"
        self.is_authenticated = False

    def check_pin(self, input_pin):
        # Check the provided PIN 
        if input_pin == self.pin:
            self.is_authenticated = True
            print("✅ PIN is correct.")
        else:
            self.is_authenticated = False  # Ensure authentication is reset on wrong PIN
            print("❎ Incorrect PIN. Access denied.")

    def check_balance(self):
        # Check the current balance
        if self.is_authenticated:
            print(f"💰 Your current balance is: ${self.balance:.2f}")
        else:
            print("🤚 Please authenticate first.")

    def deposit(self, amount):
        # Deposit an amount into the account
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(f"💵 Deposited: ${amount:.2f}. Deposited successfully.")
                print(f"💰 New balance: ${self.balance:.2f}")
            else:
                print("❎ Invalid deposit amount.")
        else:
            print("🤚 Please authenticate first.")

    def withdraw(self, amount):
        # Withdraw an amount from the account
        if self.is_authenticated:
            if amount <= 0:
                print("❎ Invalid withdrawal amount.")
            elif amount > self.balance:
                print("❎ Insufficient balance.")
            else:
                self.balance -= amount
                print(f"💲 Withdrew: ${amount:.2f}. Withdraw successful.")
                print(f"💰 New balance: ${self.balance:.2f}")
        else:
            print("🤚 Please authenticate first.")

    def exit(self):
        # Exit the ATM
        print("👋 Thank you for using the ATM. Goodbye!")
        return False  # End the loop in the main function

    def menu(self):
        # Display the ATM menu
        print("\n🏦 Welcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Please select an option (1-4): ")
        return choice


if __name__ == "__main__":
    atm = ATM()
    while True:
        choice = atm.menu()
        
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            pin = input("Enter your PIN: ")
            atm.check_pin(pin)
            if atm.is_authenticated:
                amount = float(input("Enter deposit amount: $"))
                atm.deposit(amount)
        elif choice == "3":
            pin = input("Enter your PIN: ")
            atm.check_pin(pin)
            if atm.is_authenticated:
                amount = float(input("Enter withdrawal amount: $"))
                atm.withdraw(amount)
        elif choice == "4":
            atm.exit()
            break
        else:
            print("❌ Invalid choice. Please try again.")
