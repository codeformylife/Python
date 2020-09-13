# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else : 
        count= count +1
        data= line[line.find(":")+1:].strip()
        total = total + float(data)
#print(count)
print("Average spam confidence:",total/count)
