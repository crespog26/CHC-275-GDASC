

file = open("day.txt","r") #open("<filename>","<mode>") 

buffer = file.readlines() 
names = [] 
grades = [] 
print(buffer) 
file.close() 
for line in buffer: 
    line = line.strip()
    line = line.split(",") 
    names.append(line[0])
    grades.append(line[1])
    

try:
    for i in range(len(grades)):
        grades[i] = int(grades[i])
except ValueError:
    print("grade must be a number")

print(names)
print(grades)