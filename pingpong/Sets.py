# # not ordered and not indexed
# set_one= {'ahmed', "ali", 100}
# print(set_one)
# print(set_one[0])   # Error -> Not indexed & for sure NOT slicing
#____________________________________________________
# SET has only immutable data types (Nums, strings,tuples)
#      List and Dictionary are not immutable -> mutable data can be changed

#set_two = {'osama', 100, 100.5, True, [1,2,3] } #-> Error unhashable type

# Hashing is a mechanism in Computer Science allow user to search for an object in computer memory QUICKLY

#____________________________________________________________________________
# set_two = {'osama', 100, 100.5, True, (1,2,3) }
# print(set_two) #-> working fine
#____________________________________________________________________________

# can use clear function 
# set_one= {'ahmed', "ali", 100}
# print(set_one)
# set_one.clear()
# print(set_one)
#_________________________________________________________________________

# # Can use union Function
# set_one= {'ahmed', "ali", 100}
# set_two = {'osama', 100, 100.5, True, (1,2,3) }

# print (set_one|set_two)

# print(set_one.union(set_two))

#___________________________________________________________________________

# Add Function

# D= {1,2,3,4}
# D.add (5)
# D.add(6)
# print(D)

#___________________________________________________________________________

# copy function"shallow copy"
# remove function
# discard Function & POP
# update same as union fuction
# difference to show the difference between the first set with the second set [a.difference(b)]
# difference_update to update the set with the differnce values only
# intersection() to show the similarties between two sets
#intersection_update() to update the first set with the similarities between the two sets
#symmetric_difference() to show the values in two sets that is not intersected
# issuperset() to show if the set is contain ALL the values of another set -> return True or false
# issubset() show the set is subset of another set 
# isdisjoint() to show if two sets are not intersected -> true ,,, Intersected-> False








