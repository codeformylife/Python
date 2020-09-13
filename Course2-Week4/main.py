fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    temp = line.rstrip().split()
    for line2 in temp:
        if(line2 not in lst):
   			lst.append(line2)
lst.sort()
print(lst)