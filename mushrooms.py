
small = []
medium = []
large = []

check = False
while check == False:
    option = input("Please state the mushoom size. ")
    option = option.strip().lower()
    print(option)
    if option.isnumeric():
        option = int(option)
        if option < 100:
            small.append(option)
        elif option >= 100 and option <= 200:
            medium.append(option)
        elif option > 200:
            large.append(option)
        print(small)
        print(medium)
        print(large)
    if option == "stop":
        check = True
        



