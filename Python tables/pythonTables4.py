
#Write a function SwapRows whose arguments are a table A and two integers i
#and j. The functions swaps rows i and j of A.

def main():

    
    
    A= [
        [1,2,3,4],
        [22,15,33,45],
        [0,0,1,1],
        [1,1,2,2]
       ]

    result1 = SwapRows(A,1,2)
    print(result1)

    result2 =sortAverages(A)
    print(result2)

def SwapRows(A,i,j):

    temp =  A[i]
    A[i]=   A[j]
    A[j] =  temp

    return A
#Write a program whose input is a table and the output is a table with the
#same rows that are sorted by the increasing order of their average numbers. For
#instance, for the table A as above, the resulting table will be
def sortAverages(A):
    T={}
    S=[]
    for i in range(len(A)):
        average = sum(A[i])/len(A[i])
        T[average] = A[i]
    
    for key in  sorted(T):

        S.append(T[key])
         
    
    return S
        

        

        

main()
