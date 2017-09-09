#Please write a program that will produce a report where modules are classifed according
#to the class of the received marks. In particular, the program should first print the lines
#for modules whose mark is first class (>=70) then modules with a 2:1 mark (60-69) then modules
#with a 2:2 mark (50-59), and then failed modules (mark<50). For instance, for the lists as above,
#the printout should something like the following.


Modules=["Calculus1","Calculus2","Calculus3","Programming1","Programming2","Programming3"]
Marks=[50,80,35,70,62,15]
#Modules with first class marks 
#Calculus2 80
#Programming1 70

#Modules with 2:1 marks
#Programming2 62

#Modules with 2:2 marks
#Calculus1 50

#Failed modules
#Calculus3 35
#Programming3 15

for i in range (len(Modules)):
    if (Marks[i] > 69):
        print('Modules with first class marks:')
        print(Modules[i] + '   '+ str (Marks[i]))

    if (Marks[i] >59 and Marks[i] < 70):
        print('Modules with 2:1 marks:')
        print(Modules[i] + '   '+ str (Marks[i]))

    if (Marks[i] >49 and Marks[i] < 60):
        print('Modules with 2:2 marks:')
        print(Modules[i] + '   '+ str (Marks[i]))

    if (Marks[i] < 50 ):
        print('Failed modules:')
        print(Modules[i] + '   '+ str (Marks[i]))
        
        
        
    
