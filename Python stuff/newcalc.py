
check = False
while check == False:
    print("Option 1, Addition: ")
    print("Option 2, Subtraction: ")
    print("Option 3, Multiplication: ")
    print("Option 4, Division: ")
    option = input("Select your option or quit to exit: ")
    if option == "1":
        try:
            a = input(f"Enter your first number ")
            a = int(a)
            b = input(f"Enter your second number ")
            b = int(b)
            sum = a+b
            print(sum)
        except ValueError:
            print("You have a value error")
            
    elif option == "2":
        try:
            c = input(f"Enter your first number ")
            c = int(c)
            d = input(f"Enter your second number ")
            d = int(d)
            difference = c-d
            print(difference)
        except ValueError:
            print("You have a value error")

            
    elif option == "3":
        try:
            x = input(f"Enter your first number ")
            x = int(x)
            f = input(f"Enter your second number ")
            f = int(f)
            product = x*f
            print(product)
        except ValueError:
            print("You have a value error")


    elif option == "4":
        try:
            g = input(f"Enter your first number ")
            g = int(g)
            h = input(f"Enter your second number ")
            h = int(h)
            quotient = g/h
            print(quotient)
        except ValueError and ZeroDivisionError:
            print("You have a value error or divided by zero")
        

    if option == "quit":
        try:
            check = True
        except Exception:
            print("you have an error")
    else:   
        print("please try again :C")
