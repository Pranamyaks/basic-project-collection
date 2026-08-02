def mini_atm_system(Balance,Pin):
    history=[]
    attempts=3
    while attempts>0:
       user_pin=int(input("Enter Your Pin..."))
       if(Pin==user_pin):
          print("Login succefull...")
          break
       else:
          attempts-=1
          print(f"Incorrect Pin!!..Login unsuccesfull..attempts left:{attempts}")
    if attempts==0:
       print("Too many wrong attempt card blocked..")      
       return
    while True:
       print("=====Menu=====")
       print("1.Check Balance")
       print("2.Deposite")
       print("3.Withdrawl")
       print("4.Transaction History")
       print("5.Exit")
       choice=input("Enter your choice:")
       if choice=='1':
          print(f"Your Total amount is:${Balance}")
       elif choice=='2':
          amount=float(input("Enter amount to deposit:"))
          if amount>0:
             Balance+=amount
             history.append(f"Deposited:{amount}")  
             print("Deposit is successfull..")
          else:
             print("Deposite is unsuccessfull...")   
       elif choice=='3':
          amount=float(input("Enter the amount to withdrawl:"))
          if amount<=0:
             print("Insuffient Balance..") 
          elif amount>Balance:
             print("Insuffient Balance")      
          elif amount>5000:
             print(f"One transaction you can withdraw up to Max:5000 ")
          else:
             Balance=Balance-amount
             history.append(f"withdrawed:{amount}")
             print("Withdrawed successfull...")
       elif choice=='4':
          print("===Transaction History====")
          if not history:
             print("No transaction yet...")
          else:
             for item in history:
                print('-',item)   
       elif choice=='5':
          print("thank you so much using Atm")   
          break
       else:
          print("Invalid choice..")        
mini_atm_system(12000,6361)          
                     
             


