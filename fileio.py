"""
every new account that we made, after program ends,no progress is saved

file input output way to 
most files are text files with context--noithing structurally diff from .py and .txt
    true for mostly everything

.docx are really just .txts the microsoft overhead attached to them so when microsoft word parses the file when you open it, it strips the overheadd

NEED TO KNOW 
    escape sequences
        these are sp[ecioal; characters ] put inside olur strings that format them in a certain way
            \n <= new line
    we covered exception handling for 1 particular reason: the file itself might not exist in our filesystem, we dont want program to crash if files do not exist
    
    
HOW file I/O WORKS

        
"""

msg = "hello \n world"
print(msg) #shoudl be 

"""
yopu need to clsoe a file when youre done using it. 
waste of system memory when not using it


file = open("names.txt", "r") #this will take in our list of names ad make each line 
buffer = file.readlines() 
names = []
grades = []
for line in buffer:
    line = line.strip()
    line = line.split(",") #line sis a list of elements,
    names.append(line[0]) 
    names.append(line[1])
print(names) #line [0] is the name
print(grades) #line [1] is the grade


try:
    for i in range(len(grades)):
        grades[i] = int(grades[i])
except ValueError:
    print("grade must be a number")
    
file.close() 

what if we want two separate lists of related information

what if we wanted to have names, grade in the class?

if it doesnt word, use "cd" and type name of file you want to access

have things inside comma separated
one piece of information that related 2 lists together?
    the index!
    run 2 lists joined together by their specific indices


11/3

what if nothing vchangedf about our fiel except for addiung a single record
3rd mode for opening a file called append mode





"""

names = []
grades = []
file = open("names.txt", "w") #need to tansform names and grades list so we can write it bnack 9into a file the way we want.
#writing into file step
buffer = [] #we want our lines to look like [name],[grade]
for i in range(len(names)):
    line = f"{names[i]},{grades[i]}\n"
    buffer.append(line) #just add the line back into buffer
buffer[-1] = buffer[-1].strip()
file.writelines(buffer)

file.close()

names.append("james")
grades.append("-4")