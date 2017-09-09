#Please write a function SortN ames. The argument of this function are the
#Write a program whose input are the lists are per Section 1 (names are not necessarily
#sorted). You can make the lists fixed in the program without requesting
#the user to enter them. The program should do the following.
#1. Apply the function SortN ames as per Section1 to have the lists sorted
#according to their names.
#2. Apply the function P rintT rans to have the transcript printed.
#3. Create lists BestM arks, BestLevels, BestCredits. That is, if N ames =
#[“M anagement
#, “P rogramming
#, “P rogramming], Marks = [70, 38, 65],
#Levels = [6, 5, 5], Credits = [30, 15, 15] then BestM arks[70, 65] (the mark
#38 for the “Programming” module has been omitted because there is a better
#mark for the same module), BestLevels[6, 5], Credits = [30, 15] (the
#rest of the details simply need to match the remaining modules).
#Again, the most important aspect of this task is efficiency. You should be
#able to tranverse the lists only once using a single for -loop.
#4. Use lists BestM akrs, BestLevels, BestCredits to print the graudation
#decision as per exercise 3b) of Lab Session of Week 6


from Chapter8Q1 import sortList

from Chapter8Q2 import sortListFour

def main():

    
    Names = ['Programming','Management','BCT']
    Marks = [70, 38, 65]
    Levels = [6, 5, 5]
    Credits = [30, 15, 15]

    result = sortListAll( Names,Marks,Levels,Credits)

    


def sortListAll(A,B,C,D):
    
    result_2= sortListFour(A,B,C,D)
main()
