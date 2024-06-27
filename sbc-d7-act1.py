import random

users = {}

def sign_up():
    user_id = random.randint(0, 999)
    while user_id in users:
        user_id = random.randint(0, 999)

    first_deposit = int(input("Enter amount to deposit: "))
    if first_deposit >= 0:
        users[user_id] = first_deposit
        print(f"Account Successfully Created for: {user_id}")
    else:
        print("Please Enter Proper Amount")

def delete_acc():
    if user_id in users:
        del users[user_id]
        print(f"User {user_id} has been deleted successfully!")
    else:
        print("User Id ain't found")

def withdraw():
    if user_id in users:
        if 0 < amount <= users[user_id]:
            users[user_id] -= amount
            print(f"{amount} has been withdrawn from ur account")
        else:
            print("Balance is insufficient")
    else:
        print("User Id ain't found")            
		
def deposit():
    if user_id in users:
        if amount > 0:
            users[user_id] += amount
            print(f"{amount} has been deposited to ur account")
        else:
            print("Invalid input")
    else:
        print("User Id ain't found")

def check_balance():
    if user_id in users:
        print(f"The balance for user{user_id} is currently {users[user_id]}")
    else:
        print("User Id ain't found")  
        
while True:
    print("""Menu:
          1. Create Account
          2. Check Balance
          3. Deposit
          4. Withdraw
          5. Delete Account
          6. Exit
          7. Show all user id""")

    choice = int(input("Select one operation: "))

    if choice == 1:
        sign_up()
    elif choice == 2:
        user_id = int(input("Enter User Id: "))
        check_balance()
    elif choice == 3:
        user_id = int(input("Enter user Id: "))
        amount = int(input("Enter amount to deposit: "))
        deposit()
    elif choice == 4:
        user_id = int(input("Enter User Id: "))
        amount = int(input("Enter amount to withdraw: "))
        withdraw()
    elif choice == 5:
        user_id = int(input("Enter User Id to delete: "))
        delete_acc()
    elif choice == 6:
        print("Bye!")
        break
    else:
        print("Invalid Command")                

