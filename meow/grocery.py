



print("Welcome to the grocery store!")

file = open("meow/foods.txt","r")
buffer = file.readlines() 
items = []
prices = []
file.close() 
for line in buffer:
    line = line.strip() 
    line = line.split(",") 
    items.append(line[0])
    prices.append(line[1])



check = False
while check == False: 
    print("1. add to cart")
    print("2. remove items")
    print("3. check out")
    option = input("enter your selection: ")
    if option == "1":
        print(items)
        print(prices)
        cart = input("enter the item you wish to purchase: ")
    elif option == "2":
        print(items)
        print(prices)
    elif option == "3":
        print(items)
        print(prices)
    if option == "quit":
        check = True
    else:
        print("pick something else! >:(")
    
    
    
    
    
    
    
    
    
    
    