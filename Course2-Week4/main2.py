fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
list = list()
for line in fh:
    if(line.startswith("From")):
       newline = line.rstrip().split()
       if(newline[len(newline)-1] == "2008"):
        list.append(newline[1])
        print(newline[1])
    

count = len(list)
print("There were", count, "lines in the file with From as the first word")
