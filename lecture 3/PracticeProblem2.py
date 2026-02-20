#write a program to check if a list contains a pelindrome of elements.

list=[1,2,3,2,1]
list2=list.copy()
list2.reverse()
if list==list2:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")