collection={1,2,3,4,5,5,5,6,7,8,9,"a","a","b"} #set is a collection of unordered unique items

print(collection)
print(type(collection))
print(len(collection))


empty_set=set() # to create empty set we have to use set() function because {} is used for dictionary
print(empty_set)

empty_set.add(1) # add value to set
empty_set.add(2)
empty_set.add(3)
print(empty_set)

empty_set.remove(2) # remove value from set
print(empty_set)


empty_set.clear() # remove all items from set
print(empty_set)


empty_set.add(1)
empty_set.add(2)
empty_set.add(3)

empty_set.pop() # remove random item from set
print(empty_set)

empty_set.add((4,5)) # we can add tuple to set because tuple is immutable
print(empty_set)
# empty_set.add([6,7]) # we can't add list to set because list is mutable


#union and intersection of sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}   
print(set1.union(set2)) # return a new set that contains all items from both sets
print(set1.intersection(set2)) # return a new set that contains only items that are present in both sets

