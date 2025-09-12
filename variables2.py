"""
we want keyuboard input today 

Hardcoding values is not how we use computers
We want some sort of input based on what the user does.

for example, if we wanted to have a calculator, we would want the user the be able to 
choose the numbers to bge added before runtime. thankfyukklyin python, doing this is relatively easy

there is an entire function dedicated to keybaord input

input() this does 3 things
    (1) it prints the prompts in the terminal
    (2) it scans the keyboard for input
    (3) saves the input into a variable

input("what is the first number")

Our objective is: take two numberss and add them together
"""

numsix = input("Enter your number ")
numsix = int(numsix)
lorkeez = input("Enter your second number ")
lorkeez = int(lorkeez)
sum = numsix + lorkeez
print(f"The sum is {sum}")

"""
 the user is going to type in 
 numsix = 10
 lorkeez = 5
 
 wjat dp you expect, we expect 15
 we got 105, this is not the right answer
 when it scans your keyboard, it assigns the variable to the string data type
 
 when you add strings together it just smahses them next to eachother
 
 Variables have 3 pieces of info
    (1) the name numsix
    2) string 
    3) 10
    
Typecasting = reassinging the datatype of the variable as long as its a valid target
numsix = "Jack Basmaci" <- i want to typecast this intoa  number
numsix = "10" <<- i cna typecast that

to change a str -> int
"""

