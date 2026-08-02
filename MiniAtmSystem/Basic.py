def MiniAtmSystem(Balance,Pin):
    print("Welcome To The Mini ATM System!!...")
    user_pin=int(input("Enter Your Pin"))
    if(Pin!=user_pin):
        print("Pin is incorrect Try Again..")
    else:
        while True:
            print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
            choice=int(input("Enter your choice.."))
            match(choice):
                case 1:
                    print("Your Total Balance is:",Balance)
                case 2:
                    amount=float(input("Enter Your amount"))
                    Balance=amount+Balance
                    print("Your Total Balance is:",Balance)
                case 3:
                    amount=float(input("Enter the amount you need!!"))
                    if amount<=Balance:
                        Balance=Balance-amount
                        print("Total Balance:",Balance)
                    else:
                        print("Insuffient Balance..")
                case 4:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice...")          
MiniAtmSystem(12000,6361)                      
