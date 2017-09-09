#Please write a function SortN ames. The argument of this function are the
#4 lists. The function should modify the lists so that the modules
#are sorted by the alphabetical order of their names. The data in the lists should
#be swapped so that each name matches the data in the other lists.
#For instance if Names = ['Programming',
# ,'Management'], Marks[65, 70],
#Levels = [5, 6], Credits = [15, 30] ater sorting
#Names = [“Management'
# “P rogramming00], M arks = [70, 65], Levels =
#[6, 5], Credits = [30, 15].


#section below commentd out as function is being used in Q2


#def main():

    
#    Names = ['Programming','Management']
#    Marks = [65, 70]
#    Levels = [5, 6]

#    Credits = [15, 30]

#    result = sortList( Names,Marks,Levels,Credits)

#    print(result)


def sortList(A,B,C,D):
    for i in range(len(A)-1):
       if(A[i][0]>A[i+1][0]or A[i][0]==A[i+1][0]  ):

#         temp= A[i+1]
#          A[i+1] = A[i]
#          A[i] = temp
          temp= A[i]
          A[i] = A[i+1]
          A[i+1] = temp


          temp= B[i]
          B[i] = B[i+1]
          B[i+1] = temp


          temp= C[i]
          C[i] = C[i+1]
          C[i+1] = temp


          temp= D[i]
          D[i] = D[i+1]
          D[i+1] = temp

    return (A, B, C, D)

#main()
