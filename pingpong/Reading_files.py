#workers_file=open("workers.txt","r")
#                                r+
#                                w
#                                a
#                                a+

#print(workers_file.readable())

#print(workers_file.read())

# print(workers_file.readline())

# print(workers_file.readlines())

# print(workers_file.readlines()[1])

#_____________________________________________________________________

# for workers in workers_file.readlines():
#     print(workers + " is cool")
#_____________________________________________________________________    

#workers_file.close()    #----> بتمسح الملف مش عارفة ليه المفروض تقفله بس

#_______________________________________________________________________________

#                    |   r      r+     w     w+      a      a+ 
#____________________|____________________________________________                    | 
#read                |  +      +            +               +
#write               |         +      +     +       +       +  
#create              |                +     +       +       +
#truncate            |                +     +
#position at start   |  +      +      +     +
#position at end     |                              +       +

#_______________________________________________________________________________

# workers_file=open("workers.txt","a+")
# workers_file.write("\nhunter x hunter ")
#_____________________________________________________________________________

# worker_file = open("character", "a")
# worker_file.write("\nhunter x hunter")
#_______________________________________________________________________

# worker_file = open("char", "a+")
# worker_file.write("\nhunter x hunter")
# worker_file.write("\n try hunter x hunter")
# worker_file.close()

#____________________________________________________________________________


# from os import close

# workers_file=open("workers.txt","w")
# workers_file.write("this is a new line")
# workers_file.close()
#__________________________________________________________________________

# workers_file = open("workers", "w")
# list_of_lines = ["shurooq   - programming student \n",
# "pikachu   - frontend developer\n",
# "subzero   - backend developer\n",
# "eren      - business analyst\n",
# "alchemist - data analyst\n",
# "titan     - data engineer\n" ]

# workers_file.writelines(list_of_lines)

# workers_file.close()
#___________________________________________________________________________

# workers_file = open("workers", "a+")
# workers_file.write("this is a tryline")












