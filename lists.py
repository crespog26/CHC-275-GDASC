
"""
WE CAN DO ARITHMETIC
branching control sturctures usin g if elif else some repitition 
using while loops,, can do keyboard input using inoput function
typecast variables to diff data types

the benefit of using a computer is the amount of data your computer ios capable of processing.
if i wasnt to amke some kind of related pieces of information, only way rn is to make a bunch of different variables

what happens when our data set is 100 data points long? what about a million data points long? 
creating indivicddual varaibles is a really unyielding way of going about this.
so we need some sort of way to aggragate related pieces of inbformation under one alias

lists do this in pythopn.
lists = linear ordered collections of objects under one variable's name
    = also variabkles
    
<name of the list> = [<member attributes>]
    
    
"""

mylist = [5, 10, 15, 20]
print(mylist)
# this creates our list

"""
the quesiton is: how do we access one singlular element dfro our list?

[] iondicate were wroking witha  list, we can use the swquare bracket operator on the variab;le name and place the index of the objects 

index = the numerical postition of the object within the list
"""

print(mylist[1] * mylist[3])

"""

counting in computer science stoarts at 0.

we can reassign 
"""


sum = (mylist[1] * mylist[2])
print(sum)

mylist2 = [1, 3.14, True, "hello"]
print(mylist2[2])

#cant add integer to a string

"""

mylist 2 is onf length 4
if i print mylsit2 at index 4 because you cannot access places that are not allocated yet

index out of range error is like a reading check moment 

you are trying to access soemthign you have not allocated yet

negative indices go backwards. negative numbers start at the end and go to the front (may or may not be useful in a month as of 9 25 25)

in programming there is a dewssign pattern called t4raverssing a liast
    reptiition control structure, one bny one lets us access each element of the list
    typically one a t timethere is 2 parts of this

iterator = a number that correspomnds to the c current indexc youre trying to accsss
tpically we use the letter i to denote your iterator

we will use aq while loop and an iterator to traverse our list
"""

i = 0 #curernt index is the first one, exit condxdition hitting 
while i <= 3: #this is our exit c0ndition
    print(mylist[i]) #accessing mylist at the value of the iterator is currently at
    i = i + 1 
    
    
"""

this kind of control structure is cumbersome to use
there is a second way to do a looping statement
it is almost equivalent to this

y loops,, now we can use 4 loops to do almost the same thing

for <placeholder name> in <name of the list>


it does not matter what name you use for the name of the variable name before "in"
it is not doign the same thing as y loop because 
    1) creates temporary varible assigned to the name you gave
    2) assigns temporary varible to the location you created
    3) does procedure in codeblock thenm jumps to the top, goes to next item in the list
    
num =/= mylist[i] they are two separate pleaces in memory BUT hold the same values



for loop did update the list 
for loops create copies, while loops directly access the lsit


the way weve wrottem tje while loop, weve made a huge assum ption about the list (its all integers) and (it goes up to 3)
we cannot garuntee the lists length 
    it may be length 0, length 100
    we cant asusme python knows the length of the lsit to be whats typed in there
    
there is a way to intrinsically to get the last vclaue of the list (-1) 
len(<name of the list>) = absolute lenght of the lsit
"""

mylist = [5, 10, 15, 20]
for num in mylist:
    num = num + 5
    
print(mylist)

i = 0
while i <= 3:
    mylist[i] = mylist[i] + 5
    i = i + 1
    
print(mylist)
    
print(len(mylist))
    
    