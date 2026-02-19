print("first line.\nsecond line\nthird line\ttab ")

str1="Md."
str2="Sarawer"
str3=" Bhuiyan"

name=str1+str2+str3
print(name)
print(len(name)) #print the length of a string
print(name[11])
# name[11]='_' this will show error.in python we can acces string but can't modify it.


#slicing: str[starting_indx:ending_indx]    (ending index isn't included)
print(name[3:10])
print(name[3:])
print(name[:10])
print(name[-7:-1])

#string functions
str="i am a coder."

print(str.endswith("coder.")) #return true if string ends with substring
print(str.capitalize()) #capitalise 1st char
print(str.replace('coder','programmer')) #replace all occurances of old with new substr
print(str.find("c")) #return first index of first occurrer
print(str.count('a')) #count the occurrence of substring

