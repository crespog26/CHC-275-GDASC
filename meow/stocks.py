file = open("meow/day.txt","r")
buffer = file.readlines() 
file.close()

print(buffer)

msft1 = buffer[0].strip().split(",")
msft1.pop(0)
amzn1 = buffer[1].strip().split(",")
amzn1.pop(0)
nvda1 = buffer[2].strip().split(",")
nvda1.pop(0)

msft2 = msft1
amzn2 = amzn1
nvda2 = nvda1

for i in range(len(msft2)):
    msft2[i] = int(msft2[i])

for i in range(len(amzn2)):
    amzn2[i] = int(amzn2[i])

for i in range(len(nvda2)):
    nvda2[i] = int(nvda2[i])

msft_avg1 = sum(msft2) / len(msft2)
amzn_avg1 = sum(amzn2) / len(amzn2)
nvda_avg1 = sum(nvda2) / len(nvda2)

#file2 vvv

file2 = open("meow/days.txt","r")
buffer2 = file2.readlines() 
file2.close()

print(buffer2)

msft3 = buffer2[0].strip().split(",")
msft3.pop(0)
amzn3 = buffer2[1].strip().split(",")
amzn3.pop(0)
nvda3 = buffer2[2].strip().split(",")
nvda3.pop(0)

msft4 = msft3
amzn4 = amzn3
nvda4 = nvda3

for i in range(len(msft4)):
    msft4[i] = int(msft4[i])

for i in range(len(amzn4)):
    amzn4[i] = int(amzn4[i])

for i in range(len(nvda4)):
    nvda4[i] = int(nvda4[i])

msft_avg2 = sum(msft4) / len(msft4)
amzn_avg2 = sum(amzn4) / len(amzn4)
nvda_avg2 = sum(nvda4) / len(nvda4)

#report vvv

report = open("meow/report.txt", "w")
report.write("STOCK REPORT\n")

report.write("MSFT:\n")
report.write("First 20 days: " + str(msft_avg1) + "\n")
report.write("Next 20 days:" + str(msft_avg2) + "\n")
if msft_avg2 > msft_avg1:
    report.write("Higher in days 21-40\n")
report.write("\n")

report.write("AMZN:\n")
report.write("First 20 days: " + str(amzn_avg1) + "\n")
report.write("Next 20 days:" + str(amzn_avg2) + "\n")
if amzn_avg2 > amzn_avg1:
    report.write("Higher in days 21-40\n")
report.write("\n")

report.write("NVDA:\n")
report.write("First 20 days: " + str(nvda_avg1) + "\n")
report.write("Next 20 days:" + str(nvda_avg2) +"\n")
if nvda_avg2 > nvda_avg1:
    report.write("Higher in days 21-40\n")
report.write("\n")
report.close()



