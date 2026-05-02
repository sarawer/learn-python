class A:
    varA="this is class a"

class B:
    varB="this is class B"
    
class C(A,B):
    varC="this is class C"

c=C()
print(c.varA)
print(c.varB)
print(c.varC)