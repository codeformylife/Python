name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d =dict()
for line in handle:
    line = line.rstrip().split()
    if(len(line)>3 and line[0]=="From"):
        time = line[5].split(":")[0]
        d[time]= d.get(time,0)+1

d = sorted(d.items())
for key,value in d:
    print(key,value)
        
