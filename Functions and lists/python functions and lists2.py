#This task is related to the same data as the previous one. In addition, the
#modules are assumed to be sorted according to their names (that is, the N ames
#list is sorted in the alphabetical order). Write a function P rintT rans whose
#arguments are the above lists. The function should explore the list once from
#the beginning to the end and print a transcript summarizing the results. The
#printing for each particular module should be
#Module name Level Number of Credits
#Mark 1
#Mark 2,... (provide marks for all attempts for the module)
#The most important aspect of this exercise is that you should avoid nested
#loops. Indeed, since the lists are sorted according to the names of the modules,
#instance, if module “Programming1” has been taken three times then there will
#be three consecutive entries for “Programming”. Thus the program does not
#need to “jump” forward and backward in the list to find the respective marks,
#they can be found by a straightforward exploration using a for -loop.




from Chapter8Q1 import sortList


#section below commentd out as function is being used in Q2

#def main():

    
#    Names = ['Programming','Management']
#    Marks = [65, 70]
#    Levels = [5, 6]

#    Credits = [15, 30]

#    result = sortListFour( Names,Marks,Levels,Credits)

   


def sortListFour(A,B,C,D):
    result_1 = sortList(A,B,C,D)
    

    print('Module' +'     ' + 'Mark' + '    ' + ' Level' +'     '+ ' Credits')
    
    for i in range(0,len(A)):

        print (A[i] +'     ' + str(B[i]) + '    ' + str(C[i]) +'       '+ str(D[i]))

#main()
