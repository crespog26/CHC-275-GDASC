
"""
what tio do about .pop     use .index

    amke a serpate variable czalled index 

    index = whatever
    set soem thing vlaue equal to index,, .pop on index on both lists it does what we awant

    ge tindex first
    pass index to names.pop index ajd for balances
    
depositing
    grab the name and have it correspoind to index grabbed from name
    have which acc is depositing
    
    need to grab the index
    
    index = bank1.index(name) 
    now ened to ask fro edepio amount
    money = input("how much? ")
    money = int(money)
    
    use
        access elements in lists 
        mylist [2] = value
    bank2[index] = 
    
    hailstone, x = x *3 have variable on bo0th sides
    bank2 = [index] + money
    
top tip for admin
    no pad, plain text, no overhead,, on notepad what you cAN DO IS 
        CAN HAVE 1 COLUMN FOR ACCOUND, SECONDS FOr balances, 
        hiioerm 1500,
        parisi, 10000000
        what you can do in python ios you can save another ifle in pyutho and append studff from other files to 
        
"""


bank1 = ["Mitch Schauer", "Gabby Crespo", "Colin Lawton", "Paul Gage", "Asher Collins"] #these are the "account holders", this list is where the names are stored. Important because this list is of what the "user" inputs 
bank2 = [10000, 15000, 20000, 30000, 1000] #these are the respective values for each account. this list is where each of the money values of the accounts are stored and the list that will be changed depending on which option the user chooses.
print("Welcome to First Financial Credit Union!")

check = False
while check == False: #this while loop is used to loop the program :)
    for i in range(len(bank1)): 
        print(f"Account holder: '{bank1[i]}' Account balance: '{bank2[i]}'") #this prints both lists every time one of the options is completed at the start of every loop
    print("1. Add Account")
    print("2. Remove Account")
    print("3. Make a Deposit")
    print("4. Withdrawal")
    print("5. Transfer Funds")
    option = input("Select your option or quit to exit: ")
    if option == "1":
        name = input("Add account: ") #this creates the variable for the name that will be added to bank1
        bank1.append(name) #this is it actually being added
        bal = input("How much money is in your account? ") #asking for the value of the varible that is going to be added to bank2
        bal = int(bal) #typecasting bal to be an integer
        bank2.append(bal) #adding the new variable to the list
    elif option == "2":
        name = input("Remove account: ") #user inputs one of the names form the list to sekect it
        index = bank1.index(name)
        bank1.pop(index) #this deletes the corresponding part of the list from bank1!
        bank2.pop #same as above, but for bank2
    elif option == "3":
        name = input("Which account is depostiing? ")
        index = bank1.index(name)
        money = input("State the amount being deposited: ")
        money = int(money)
        bank2[index] =  bank2[index] + money
    elif option == "4":
        name = input("Which account is withdrawing? ")
        index = bank1.index(name)
        money = input("State the amount being withdrawn: ")
        money = int(money)
        bank2[index] =  bank2[index] - money
    elif option == "5":
        name = input("Which account is making the transfer?: ")
        index = bank1.index(name)
        name2 = input("To which account?: ")
        index2 = bank1.index(name2)
        transfer = input("State the amount being transferred: ")
        transfer = int(transfer)
        bank2[index] = bank2[index] - transfer
        bank2[index2] = bank2[index2] + transfer
    if option == "quit":
        check = True












