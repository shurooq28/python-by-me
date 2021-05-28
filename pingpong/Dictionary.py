# user = { "name":"shurooq",
#  "country" : "Egypt",
#  "job": "Engineer"
#  }
# print(user) 
#________________________________________________________________________

# print(user["country"])
# #OR
# print(user.get("country"))

# print(user.keys())
# print(user.values())
#_________________________________________________________________________

# Nested dictionary or 2D dictionary

# languages={
#     "first_lan": {
#         "name": "html",
#         "progress":"20%"
#     },
#     "second_lan":{
#         "name":"python",
#         "progress":"90%"
#     }
# }

# #print(languages)
# #print(languages["first_lan"])
# # print(languages["first_lan"]["name"])
# print(len(languages))
# print(len(languages["second_lan"]))
#________________________________________________________________________

# language_one = {
#         "name": "html",
#         "progress":"20%"
#     }

# language_two= {
#      "name":"python",
#         "progress":"90%"
#     }

# All_languages = {
#     "first":language_one,
#     "second":language_two
# }

# print(All_languages)

#________________________________________________________________________

# Update()

# member= {
#     "name":"shurooq"
# }

#_____ first method________

# print(member)
# member["age"]=27
# print(member)

#______Second method________

# member.update({"country":"Egypt",})
# print(member)

#_________________________________________________________________________

# user= {
#     "name":"shurooq",
#     "age":"28",
#     "country":"egypt",
#     "skills":["C", "python","C++"],
#     "rating":9.5
# # }
# print(user)

# print(user.["country"])

# # print(user.get("country"))

# print(user.keys())    ----------> to print all keys of Dictionary

# print(user.valuess()) ----------> to print all values of Dictionary
#____________________________________________________________________

# Two dimentional dictionary ( Nested Dictionary )

# languages= {

#       "one":{
#         "name":"python",
#         "progress":"60%"       
#       },
#     "two": {
#         "name":"C",
#         "progress":"50%"       
#     }

# }

# print(languages)

# print(languages["one"])

# print(languages["two"]["progress"])

# print(len(languages))

# print(len(languages["two"]))
#_____________________________________________________________________

#languages.clear() -------> to clear the whole dictionary

#_____________________________________________________________________

#_______copy fuction____________

# main={
#     "name":"shurooq"
# }

# b=main.copy()
# print(b)
# main.update({"skills":"fighting"})
# print(main)
# print(b)

#_____________________________________________________________________

# user = {
#     "name":"shurooq"
# }

# print(user)

# user.setdefault("age",36)

# user.setdefault("name","ahmed") 

# print(user)

# #____________________________________________________________________
   ############## Difference between pop() & popitem()

# member= {
#     "name":"shurooq",
#     "skills":"python"
# }

# print(member)
# member.update({"age":28})
# print(member)
# print(member.pop("name")) #-------> delete the given key from the dictionary
# print(member)
# print(member.popitem())  #------> to delete the last item has been added to dictionary
# print(member)

#____________________________________________________________________

# .items()

# .fromkeys()










#____________________________________________________________________










