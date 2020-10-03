class Students:
  

   def __init__(self, name, age, testScore):
      self.name = name
      self.age = age
      self.testScore = testScore

   

   def displayStudent(self):
      print ("Name : ", self.name,  ", Age: ", self.age,  ", Test Score: ", self.testScore)


lst = list()

lst.append(Students('thien',20,10))
lst.append(Students('linh',18,10))
lst.append(Students('tuan',19,9))
lst.append(Students('kien',20,10))
lst.append(Students('long',20,2))
lst.append(Students('da',22,7))
print('list Student :')
for item in lst:
    item.displayStudent()

for i in range(int(len(lst))):
    for j in range(int(len(lst))):
        if(lst[i].age > lst[j].age):
            temp = lst[i]
            lst[i]=lst[j]
            lst[j]=temp

print('\nlist Student sorted by desceasing age :')
for item in lst:
    item.displayStudent()