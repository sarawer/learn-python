marks=[67,93,50,43.4,"a","string"] #list can store diffrent type of data
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

student=["sarawer",528,3.38]
student[0]="rahat"
student[1]=527
student[2]=3.91
print(student)

#list methods
list=[2,9,5,0,1,0]

list.append(10)
list.sort() #ascending
list.sort(reverse=True) #descending
list.insert(5,20)
list.reverse() 
list.remove(0)  #remove value
list.pop(0) #remove value on index
print(list)
