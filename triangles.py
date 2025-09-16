"""
be careful because if one condition suceeds then all conditions below will not run

There are times wherer you want to exaluate more than opne conditional
<condition> AND <other condition> 

how do in python?

"""

angle1 = input("enter angle one ")
angle1 = int(angle1)
angle2 = input("enter angle two ")
angle2 = int(angle2)
angle3 = input("enter angle three ")
angle3 = int(angle3)

"""
lets check if its a triangle
there is no symbol for and / or, you cand just use the words

we need to find a way to make sure we can have every valid comination of angle123 to make a valid triangel
OR

if you wrap two or more confitionals into one conditional usiong parentheses, you can reframe the two conditionals to ecactly oner conditional
A        B          A and B
t         f          f
f          t         f
f         f           f
t         t           t
"""

if (angle1 == 90 and angle2 + angle3 == 90) or (angle2 == 90 and angle1 + angle3 == 90):
    print("this is a triangle")

