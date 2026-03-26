#find the factorial of first n numbers

#using while loop
n=5
fact=1
while(n!=0):
    fact*=n
    n-=1

print(fact)


#using for loop
n=5
fact=1

for i in range(1,n+1):
    fact*=i

print(fact)