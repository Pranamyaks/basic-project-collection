File_Name='contacts.txt'
while True:
    print("Contact Book")
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Exit")
    try:
        choice=int(input("Enter your choice:"))
    except:
        print("Invalid choice!!Try again")
        continue
    if choice==1:
        name=input("Enter your name:")
        Phone=input("Enter your mobile number:")
        try:
            with open(File_Name,'a') as file:
                file.write(name+','+Phone+'\n')
            print("Contact saved successfully!!")
        except:
            print("Error Saving contact!!..")
    elif choice==2:
        try:
            with open(File_Name,'r') as file:
                print("---Contact List---")
                for line in file:
                    line=line.strip()
                    if line:
                        name,Phone=line.split(',')
                        print("Name:",name,"|Phone:",Phone)
        except FileNotFoundError:
            print("no contacts Found")
    elif choice==3:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice!!Please try again...")                        
