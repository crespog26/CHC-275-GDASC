
"""
lets talk about everyhting w eknow about lists

what is a lisxt?
- sequence of objects
-muteable (can change in length)
- mixed data types
- a list is also an object
- theoretically we could store lists inside of lists
"""

grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]


]


"""


we can access dinividual elements by using mylist[index]

grid[row][column]

"""


box = [
    [1,2,3],
    [4,5,6],
    [7,8,9]    
]

print(box[0][0])

"""
2d lists row top to bottom, left to right.
    as the firdst index grows, we are moving down the rows 
    as we increment second index, we are moving to the right of each column

we dont always have to use seocn dsquare brackets to get stuff out of the list

"""

print(box[1])
"""
only sort of consideration to be made is top 
based on the structure of this thing here, do we believe there is an easy way to pull out a single column
    - NO

let's talk about iterating over a 2d list
2 indices to keep track of
3 kinds of loopnig statements
- for each
    - least flexibility, easiest to use
-for i loops
    - hard to use, easy flexibility
-while 
    - most difficult to use, lots of flexibility in terms of stopping conditions, etc.

we are going to do a loopig  statement over all the numbers ina  2d lsit
how many for each loops do you think we'll need?
    2, one for rows and one for columns
we need two loops, an outer loop and an inner loop

outer loop is for rows, inner loop is for every single number in a row.
every row then every single number inside the row
row --> grid 

inner loop 

"""

#what is the data type of row?
for row in box:
    for num in row:
        print(num)
    
"""
easy to use, nomenclature may be different 
we are pulling out rows and then numbers from each row


for i loops requeire a few things
- range of values
- counting variable
- need a length to pass into range

"""

box2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

for i in range(len(box2)):
    for j in range(len(box2[0])): # 0-3
        print(f" (i),(j) = {box2[i],[j]}", end = "")