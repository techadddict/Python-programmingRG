#5. Write a program whose input is a list ListStr of strings, all strings being
#of the same length m. Let n = len(ListStr) Write a program that works
#as follows.
#(a) Explores all i from 0 to m − 1.

#(b) For each i, the program creates a string ColStr consisting of the i-th
#symbols of the elements of ListStr. Formally, ColStr = ListStr[0][i]+
#ListStr[1][i] + . . . + ListStr[n − 1][i]. For instance, if ListStr =
#[”abc”, ”ced”, ”beg”, ”ofg”] and i = 1 then ColStr should be ”beef”.
#Then the program prints resulting string ColStr.

def main():
    
    ListStr=['abc', 'ced', 'beg', 'ofg']
    mySolution = createString(ListStr,1)
    print(mySolution)

def createString(A,n):
    newString = ''
    for i in range (len(A)):
        newString = newString  +  A[i][n]
    return newString


main()
