#function swaps elemnts in given positions in the list 
def main():
    A=[8,5,7,15,9]
    b=SwapLst(A,1,3)
    print(b)

    

def SwapLst(A,i,j):
    
    temp =A[i]
    A[i]=A[j]
    A[j]=temp
    return A

main()
