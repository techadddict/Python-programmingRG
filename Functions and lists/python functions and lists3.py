#Write a program whose input are two lists A and B. The program should
#print YES if there is an element A[i] of A and B[j] of B such that B[j] ≥
#A[i] + 20. Otherwise, the program should print NO.



def main ():
    X = [3,5,6,7,4,9]
    Z= [2,0,0,0,2,2]
    

    test = checkLists_AB(X,Z)
    
def checkLists_AB(A,B):
    found=0
    for i in range(len(A)):
        for j in range(len(B)):
            if ( (B[j] == (A[i] + 20)) or (B[j] > (A[i] + 20))):
                found = 1
                break
    if (found == 1):
        
        print('Yes')
    else:
        print('No')



main()
