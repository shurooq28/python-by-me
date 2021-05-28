 #friends = [1, "codezilla", True, False, [1, "islam"]]
# tutorial=["extend", "list", "codezilla"]
#____________________________________________________________
#first methode of concatenation 
#print(friends, tutorial)
#___________________________________________________________
#second methode of concatenation
#friends.extend(tutorial)
#print(friends)
#____________________________________________________________
#third methode of cocatenation
#friends+=tutorial
#print (friends)
#____________________________________________________________
#Append Function -> to add a new value to the last index of the list
#friends.append('islam')
#print(friends)
#_____________________________________________________________
#insert Function -> to insert any value to the list in any index
#friends.insert(1,"islam")
#print(friends) #this will add "islam" in index 1 of the list friends
#_____________________________________________________________
#Function remove -> to remove aspecific value from the list
#friends.remove([1, "islam"])
#print(friends) 
#______________________________________________________________
#function clear -> it clear the whole list
#friends.clear()
#print(friends)
#_______________________________________________________________
# #Fuction POP -> clear the last value in the list and can save this value
# friends = [1, "codezilla", True, False, [1, "islam"]]
# #friends.pop()
# print(friends.pop())
# print(friends)
#___________
#what_was_poped = friends.pop()
#print(what_was_poped)
#________________________________________________________________
#function index to get the indes of the variable in the list
#print(friends.index("codezilla"))
#_________________________________________________________________
#fuction count -> to count how much does this variable appear in the list
#print(friends.count(1)) #----> this will give me 2 counts
# ____________________________________________________________________
#num = [1,4,6,2,5,3]
#num.sort()
#print(num)
#____________________________________________________________________
#function copy -> this fuction do not affected by any opperation done over the original list
#new_list = friends.copy()
#print(friends)
#print(new_list)  # this is shallow copy
#friends.append('programming')
#print(friends)
#______________________________________________________________________
 # two dimentinal list 

# no_list = [
#     #column 0  #column 1   #column 2
#     [1,          2,          3],            #row 0
#     [4,          5,          6],            #row 1
#     [7,          8,          9],            #row 2
#     [0                        ]             #row 3
# ]

# print(no_list[3][0])





