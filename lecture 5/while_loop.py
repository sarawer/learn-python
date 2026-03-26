#print 1 to 100
i=1
while (i<=100):
    print(i)
    i+=1
print("loop ended here")

#print 100 to 1
i=100
while (i>0):
    print(i)
    i-=1
print("loop ended here")

#print mmultiplication table of n

i=1
n=5

while(i<=10):
    print(n*i)
    i+=1
print("loop ended")


#print the elements of the following list using loop:
list=[1,4,9,16,15,36,49,64,81,100]
i=0
while(i<len(list)):
    print(list[i])
    i+=1

# search for a number x in this tuple using loop
tup=(1,4,9,16,15,36,49,64,81,100)
x=100
i=0
while(i<len(tup)):
    if(tup[i]==x):
        print("found at index ",i)
        break
    else:
        i+=1
