

file = open("day.txt","r")
buffer = file.readlines() 
file.close()
print(buffer)
msft = (buffer[0])
amzn = (buffer[1])
nvda = (buffer[2])
msft = buffer.strip().split(",")
msft.pop(0)
amzn = buffer.strip().split(",")
amzn.pop(0)
nvda = buffer.strip().split(",")
nvda.pop(0)

for i in range(len(msft)):
    i = int(i)