#func definition
def calc_sum(a,b): #peremeters
    return a+b


sum=calc_sum(10,12) #functon call
print(sum)


def print_hello():
    print("hello")

print_hello()


def calc_avg(a,b,c):
    return (a+b+c)/3

avg=calc_avg(12,45,32)
print(avg)


def calc_mul(a,b=2): # default argument
    return a*b

mul=calc_mul(3)
print(mul)

#print the length of a list:
def list_len(list):
    print(len(list))

names=["sarawer","rahat","niloy","mahir"]
cities=["dhaka","comilla","chattagram","noakhali","feni"]
# list_len(names)
# list_len(cities)

# print the elements of a list in a single line:
def ele_list(list):
    print(list)

ele_list(names)

#find the factorial of n
def calc_fact(n):
    fact=1
    for i in range(1,n+1,1):
            fact*=i
    print(fact)

calc_fact(5)

#convert usd to bdt
def usd_to_bdt(x):
        print(x*122.7271)

usd_to_bdt(100)