



print(f"Welcome to the docks! go fishing.")
print("Option 1: carnivorous.")
print("Option 2: saltwater.")
print("Option 3: community.")
fishy1 = input(f"what kind of fish do you have? ")
if fishy1 == ("carnivorous"):
    fishy2 = input(f"do you already have it? ")
    if fishy2 == ("yes"):
        print("TOO BAD")
    elif fishy2 == ("no"):
        print("enjoy! :3")
    else:
        print("try again.")
elif fishy1 == ("saltwater"):
    print("you're a fancy fish parent! :O")
elif fishy1 == ("community"):
    print("you should get more than one!")
else:
    print("I dont think that's a type of fish.")