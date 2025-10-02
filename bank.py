
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


bank1 = ["Mitch Schauer", "Gabby Crespo", "Colin Lawton", "Paul Gage", "Asher Collins"]
bank2 = [10000, 15000, 20000, 30000, 1000]
print("Welcome to First Financial Credit Union!")

check = False
while check == False:
    for i in range(len(bank1)):
        print(f"Account holder: '{bank1[i]}' Account balance: '{bank2[i]}'")
    print("1. Add Account")
    print("2. Remove Account")
    print("3. Make a Deposit")
    print("4. Withdrawal")
    print("5. Transfer Funds")
    option = input("Select your option or quit to exit: ")
    if option == "1":
        name = input("Add account: ")
        bank1.append(name) 
        bal = input("How much money is in your account? ")
        bal = int(bal)
        bank2.append(bal)
    elif option == "2":
        name = input("Remove account: ")
        index = bank1.append(name)
        bank1.pop(index)
        bank2.pop(index)
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












