"""
lets discuss froom a software development standpoint how if elifs can be used ina  software design question

when you launch a game you open to a main menu,, when we typically want some sort of main menu in our command line programs

1. print out all of the options
2. take in keyboard input
3. uuse ids and elifs in order to sleect the option the usr typed in 

fresh 5 soph 7 junior 10 senrior 11
"""
print("Welcome to the lunch loan program")
print("1. Freshman")
print("2. Sophomore")
print("3. Junior")
print("4. Senior")
option = input("Enter your grade level ")

if option == "Freshman":
    print("you get 5 dollars!")
if option == "Sohomore":
    print("you get 7 dollars!")
if option == "Junior":
    print("you get 9 dollars!")
if option == "Senior":
    print("you get 11 dollars!")