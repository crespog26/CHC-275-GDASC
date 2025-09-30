




"""
for loops make copies of elements instead of just copying them,, for num did not update the list.

rather than traversing the list of elements ina  for loop, an equallyt vvviable option is to travese the indices instead. 

2 NEW FDUNCTIONS
range(<name of list>) <= creates a ;ost pf mi,ners corresponding to thje indices of a list

len(<name of list>) tjos retirms the lnegth of the list 

would make copies of elements,, why dont we make copies of the indices of the list,, 



mylist = [10, 20, 30, 40, 50,]
        #0. 1. 2. 3. .4        would you say the indices also count as an ordered sequence of elements? YES 
        
for i in range(len(mylist)): 
    print(mylist[i])
    
for num in mylist:
    print(num)
    
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1



print('example 2')
for i in range(len(mylist[i])):
    mylist[i] + 5
print(mylist)



print("example 3")
names = ["john", "joe", "paul"]
print(names)

names.append("zack")
print(names)

names.remove("joe")
print(names)
names.pop(0)

print("example 4")
names = []
check = False
while check == False:
    name = input("Enter the name you want to add to the list: ")
    if name == "quit":
        check = True
    else:
        names.append(name)
        
print(names)"""

print("example 4")
students = ["john", "zach", "paul"]
GPAs = [88, 71, 85]

for i in range(len{students[i]}):
    print(f"Student: {students[i]} GPA: {GPAs[i]}")
    

"""
need a way to searhc our list

how to get indices out from list
without looking at the code
"""