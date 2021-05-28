# # str()

# a=10
# print(type(a))
# print(type(str(a)))
#______________________________________________________________________

# Tuple() conversion

# c="shurooq"        #string
# d=[1,2,3,4,5]      #List
# e={"A","B","C"}    #Set
# f={"A":1, "B":2}   #Dictionary

# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))

#print(tuple(500)) #can only change iterable data--TypeError: 'int' object is not iterable

#______________________________________________________________________


# List() conversion

# c= "shurooq"       #string
# d=(1,2,3,4,5)      #Tuple
# e={"A","B","C"}    #Set
# f={"A":1, "B":2}   #Dictionary

# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))

#_________________________________________________________________________

# Set() Conversion

# c= "shurooq"       #string
# d=(1,2,3,4,5)      #Tuple
# e=["A","B","C"]    #List
# f={"A":1, "B":2}   #Dictionary

# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))

#_____________________________________________________________________
 
# Dic() Conversion  -------->> ERROR


# c= "shurooq"       #string ---> Error
# d=(1,2,3,4,5)      #Tuple  ---> Must be nested tuple
# e=["A","B","C"]    #List   ---> Must be nested List
# f={"A","B"}        #Set    ---> Error -> unhashable type

# print(dict(c))
# print(dict(d))
# print(dict(e))
# print(dict(f)) 
#_________________________________________

# Nested Tuple converted to dictionary

# d=(("A",1),("B",2),("C",3),("D",4))
# print(dict(d))

#_________________________________________

# Nested List converted to dictionary

# e=[["one",1],["two",2],["three",3]]
# print(dict(e))

#___________________________________________________________________




