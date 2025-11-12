

file = open("day.txt","r")
buffer = file.readlines() 
file.close()
print(buffer)
msft = (buffer[0])
amzn = (buffer[1])
nvda = (buffer[2])
msft = buffer.split(",")
msft.pop(0)
amzn = buffer.split(",")
amzn.pop(0)
nvda = buffer.split(",")
nvda.pop(0)

for i in msft:
    i = int(i)