#Reports printing
#The following two exercises are a little bit more `real-life-like'.
#Both programs hold two lists: Modules and Marks representing the list of
#modules studied by a student and respective marks.
#For instance if
#Modules=["Calculus1","Calculus2","Calculus3","Programming1","Programming2","Programming3"]
#and Marks=Marks=[50,80,35,70,62,15] then this means that the mark for Calculus1 is 50,
#the mark for Calculus2 is 80 and so on.
#To save time of typing these lists every time you run the programs, you can assume that
#these lists are initially assigned inside your programs, e.g. as above, and the programs will
#should work correctly for lists with any content, not just the one you have tested them on.

#2.1. Please write a program that prints the modules and lists in a report like form
#module  mark' per line. For instance, for the above lists the corresponding printout will be
#Calculus1 50
#Calculus2 80
#Calculus3 35
#Programming1 70

Modules=["Calculus1","Calculus2","Calculus3","Programming1","Programming2","Programming3"]
Marks=Marks=[50,80,35,70,62,15]
for i in range(len(Modules)):
    print( Modules[i] + '               '+ str( Marks[i]))
