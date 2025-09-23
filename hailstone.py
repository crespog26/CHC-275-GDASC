"""
use mod %

if thigny = 1 check false
"""


check = False
while check == False: 
    x = input("enter your number. ")
    x = int(x)
    print(x)
    if x % 2 == 1:
        x = (x * 3 + 1)
        print(x)
    elif x % 2 == 0:
        x = x/2
        print(x)
    if x == (1):
        check = True
