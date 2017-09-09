#This exercise is similar to the previous one with the difference that only
#one list is considered. Write a program whose input is a list A. The
#program should print YES if A contains two elements whose difference is
#20 or more. Otherwise, the program should print NO.


def main ():
    X = [3,5,6,73,4,9]
    
    

    test = checkList_A(X)
    
def checkList_A(A):
    found=0
    for i in range(len(A)):
        for j in range(len(A)):
            if ( (A[j] == (A[i] + 20)) or (A[j] > (A[i] + 20))):
                found = 1
                break
    if (found == 1):
        
        print('Yes')
    else:
        print('No')



main()
