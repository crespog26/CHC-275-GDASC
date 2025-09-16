"""

When we run a calcx program, we expect to b abnle to choose which operation we want to do
from a list of options

Having some sort of main menu protocol on our control structure.

control sturctures = individualizations in our program
    - sepquential (lines running one after another)
    - branching 
    - repetition
    
branching = we want some code blocks to be based on certian conditions being met within our program

strings, integers, floats, boolean

boolean = true or false

conditional = some logical statement that can be evaluated to a boolean value
            = some english statement that is either true or false
            
if conditional:
    <MUST BE CODED OVER code blocks>
    
if (conditional) {}
modulus = % 
what modulus does divide a by b and returns the remainder
a % b = a mod b = the remainder after a/b

we can use modules to check for divisibility rules, for a number to be divisibl4e by 2

a % 2 = 0

ONE EQUALS is for variable assignment. TWO EQUALS is for equality chekcing
"""

x = 10
if x % 2 == 0:
    #if x mod 2 is equal to 0, run the code block below
    print(f"{x} is divisible by 2")
    if x % 4 == 0:
        print(f"{x} is divisible by 4")
elif x % 3 == 0:
    print(f"{x} is divisible by 3")
else:
    print("fail condition")

"""
error checklist:
    - make sure you have acolon after the if statement
    - make sure the code block under the if statement is tabbed over
    - make sure every line of code under the if statement has the same amount of white space
    
VS CODE TOP TIP
    
    if you highlight all of the whitespace, youll be able to see how many spaces there are
    
what if we want to check some other condition in another language?

    if
        thing
    
elif has to be on the same tab lavel as then if statemnt its related to

what is the difference between 
"""

if x % 2 == 0:
    print(f"{x} is divisible by 2")
elif x % 5 == 0:
    print(f"{x} is divisible by 5")
    
    
if x % 2 == 0:
    print(f"{x} is divisible by 2")
if x % 5 == 0:
    print(f"{x} is divisible by 5")
    
"""
be careful because if one condition suceeds then all conditions below will not run

There are times wherer you want to exaluate more than opne conditional
<condition> AND <other condition> 

how do in python?

"""