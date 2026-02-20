tup = (1, 2, 3, 3, 6, 2, 8, 2)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1:6])
# tup[0] = 4 #this will give error because tuples are immutable


#touple methods
print(tup.count(2)) #return the number of times a value occurs in the tuple
print(tup.index(2)) #return the index of the first occurrence of the value