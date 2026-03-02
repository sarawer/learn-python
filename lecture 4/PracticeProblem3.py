'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one.
Use subject name as key & marks as value.
'''

marks={}

a=int(input("enter marks of phy:"))
b=int(input("enter marks of chem:"))
c=int(input("enter marks of bio:"))


marks.update({
    "physics":a,
    "chemistry":b,
    "biology":c

})

print(marks)