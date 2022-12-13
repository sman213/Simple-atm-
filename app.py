from platform import python_branch
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")




print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN:")
balance = 0
print(name, "has been registered with a starting balance of $"+ str(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name2 = input("Enter name: ")
    pin2 = input("Enter PIN: ")
    if name2 == name and pin2 == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid Credentials!")
        continue
while True:
  
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":               
        account.show_balance(balance)
    elif option == "2":             
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":             
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option =="4":                           
        account.logout(name)
        break
    else:
        atm_menu(name)
        print("Invalid Selection, please choose options 1-4")
        continue
        