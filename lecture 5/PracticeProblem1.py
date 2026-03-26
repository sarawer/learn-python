#find the sum of first n natural numbers 

#using while loop
n=5
sum=0

while(n!=0):
    sum+=n
    n-=1

print(sum)

#using for loop
n=5
sum=0

for i in range(1,n+1):
    sum+=i

print(sum)