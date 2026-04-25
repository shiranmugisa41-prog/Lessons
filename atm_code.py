# Improved ATM Program (Error Fixed)
# Hello Shiran this is great work, for your next assignment please remember to include comments atleast for each block of code. 
# I am cheering you 

accounts = {
    "1001": {
        "name": "John",
        "pin": "1234",
        "balance": 10000.0,
        "history": []
    },
    "1002": {
        "name": "Sarah",
        "pin": "5678",
        "balance": 8000.0,
        "history": []
    }
}


def get_amount(message):
    try:
        amount = float(input(message))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return None
        return amount
    except ValueError:
        print("Invalid number entered.")
        return None


# Login
acc_no = input("Enter Account Number: ").strip()
pin = input("Enter PIN: ").strip()

if acc_no in accounts and accounts[acc_no]["pin"] == pin:

    user = accounts[acc_no]

    print("\nWelcome", user["name"])

    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Exit")

        option = input("Choose option: ").strip()

        if option == "1":
            print(f"Balance: {user['balance']}")

        elif option == "2":
            amount = get_amount("Amount to deposit: ")
            if amount:
                user["balance"] += amount
                user["history"].append(f"Deposited {amount}")
                print("Deposit successful.")

        elif option == "3":
            amount = get_amount("Amount to withdraw: ")
            if amount:
                if amount <= user["balance"]:
                    user["balance"] -= amount
                    user["history"].append(f"Withdrew {amount}")
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds.")

        elif option == "4":
            receiver = input("Receiver Account Number: ").strip()

            if receiver in accounts and receiver != acc_no:
                amount = get_amount("Transfer amount: ")

                if amount:
                    if amount <= user["balance"]:
                        user["balance"] -= amount
                        accounts[receiver]["balance"] += amount

                        user["history"].append(
                            f"Transferred {amount} to {receiver}"
                        )
                        accounts[receiver]["history"].append(
                            f"Received {amount} from {acc_no}"
                        )

                        print("Transfer successful.")
                    else:
                        print("Insufficient funds.")
            else:
                print("Invalid receiver account.")

        elif option == "5":
            print("\nTransaction History")
            if not user["history"]:
                print("No transactions yet.")
            else:
                for item in user["history"]:
                    print("-", item)

        elif option == "6":
            new_pin = input("Enter new 4-digit PIN: ").strip()

            if len(new_pin) == 4 and new_pin.isdigit():
                user["pin"] = new_pin
                print("PIN changed successfully.")
            else:
                print("PIN must be exactly 4 digits.")

        elif option == "7":
            print("Thank you for banking with us.")
            break

        else:
            print("Invalid choice. Try again.")

else:
    print("Wrong account number or PIN.")
