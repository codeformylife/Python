
import re

data = open("Course3-Week2\data.txt")
total=0
for line in data:
     listDigit = re.findall('[0-9]+',line)
     if(len(listDigit)>0):
         for item in listDigit:
            total = total + int(item)
print(total)