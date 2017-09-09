#Write a program whose whose input is a list of strings. The program
#should print the number of strings in the list where all the symbols are
#the same (e.g. “aaaaaaa” or “777777777777”).


def main():
    
    B=['BBKB','CCHC','GGGG','YYYY','LILL']

    test= checkLettersInList(B)
    print(test)

def checkLettersInList(X):
    count=0
    for i in range (len(X)):
        if(checkLetters(X[i])==1):
           count=count + 1
    return count
           

    
def checkLetters(A):    
    nfound = 1
    count=0
    for i in range(len(A)):
        for j in range(len(A)):
            if(A[i] != A[j]):
               nfound =0
    return nfound

    
main()
