name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict = dict()
for line in handle :
    line = line.rstrip().split()
    if(len(line)>3 and line[0]=="From") :
       dict[line[1]]=dict.get(line[1],0) + 1
max = 0
keymax= ""
for key,value in dict.items() :
    if(value > max):
        max = value
        keymax = key
print(keymax +" "+str(max))	