#A table B is a transpose of a table A if for any two indices i and j B[i][j] =
#A[j][i]. In other words, B is obtained from A by treating the rows of A as
#columns and the columns as rows.
#In the following example B is a transpose of A.
#1 2 3 4 1 22 0 1
#A= 22 15 33 45 B= 2 15 0 1
#0 0 1 1 3 33 1 2
#1 1 2 2 4 45 1 2
#Write a function whose whose argument is a table and which returns its
#transpose


def main():

    A= [
        [1,2,3,4],
        [22,15,33,45],
        [0,0,1,1],
        [1,1,2,2]
       ]
    result =transposeTable(A)
    print(result)
    
def transposeTable(A):
    B=[]
    for i in range(len(A)):
        T=[]
        for j in range(len(A)):
            T.append(A[j][i])
        B.append(T)
    return B

main()
    
