# An element A[i] of a list A is an *extreme point* of A if the following two conditions
#   are true.
#   - A[i] is neither the first nor the last element. That is, 0<i<n-1.
#  - A[i-1]>A[i]<A[i+1] or A[i-1]<A[i]>A[i+1].
#   For instance, the extreme points of the list [0,5,3,6,8,7,15,9] are 5,3,8,7,15.
   
#   a) Write a function whose arguments are a list A and an integer 0 such
#      that 0<i<len(A) (you can assume that i is within that range and not
#      to check the validity of the argument within the function).
#      The function returns 1 if A[i] is an extreme element of A and 0 otherwise.

#   b)  Use the function of part a) to write a program that obtains a list A 
#       from the user and prints all the extreme elements of A.
#       Hint: explore the array in a for loop and for each value of the counter 
#       i, run the above function with arguments A and i.


def main():
    A= [0,5,3,6,8,7,15,9]
    b= Extreme_PointC(A)
    c=Extreme_Point(A,1)
   # print(b)
    print(c)
    

def Extreme_PointC(A):
    for i in range (1,len(A)-1):
         if(A[i]!= len(A)-1):
            if((A[i-1]>A[i]<A[i+1] or A[i-1]<A[i]>A[i+1])):
               return (A[i])
    #return


def Extreme_Point(A,j):
    for i in range (1,len(A)-1):
         #if(i!= len(A)-1):
          if((A[i-1]>A[i]<A[i+1] or A[i-1]<A[i]>A[i+1])):
               return 1
    return 0
       


main()
