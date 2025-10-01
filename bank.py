
"""
what tio do about .pop     use .index

    amke a serpate variable czalled index 

    index = whatever
    set soem thing vlaue equal to index,, .pop on index on both lists it does what we awant

    ge tindex first
    pass index to names.pop index ajd for balances
    

"""


bank1 = ["Mitch Schauer", "Gabby Crespo", "Colin Lawton", "Paul Gage", "Asher Collins"]
bank2 = [10000, 15000, 20000, 30000, 1000]
print("Welcome to First Financial Credit Union!")

check = False
while check == False:
    for i in range(len(bank1)):
        print(f"Account holder: '{bank1[i]}' Account balance: '{bank2[i]}'")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. Transfer funds")
    option = input("Select your option or quit to exit: ")
    if option == "1":
        name = input("Add Account: ")
        bank1.append(name) 
        bal = input("How much money is in your account? ")
        bal = int(bal)
        bank2.append(bal)
    elif option == "2":
        print("2")
    elif option == "3":
        print("3")
    if option == "quit":
        check = True












