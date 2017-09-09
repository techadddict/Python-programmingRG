#6. Let a and b be two digits. Their sum modulo 10 is a+b in case a+b < 10
#and a + b − 10 otherwise. For instance, the sum of 3 and 5 modulo 10 is
#8 while the sum of 7 and 8 modulo 10 is 5.
#(a) Write a function whose arguments are two digits. The function should
#return their sum modulo 10.
#(b) Let Str1 and Str2 be two strings of the same length m whose symbols
#are digits. Then the sum of Str1 and Str2 modul0 10 is the string
#Str of length m such that for each i from 0 to m − 1, Str[i] is the
#sum of Str1[i] and Str2[i] modulo 10. For instance, the sum of “13500
#and “92800 modulo 10 is “05300
#.
#Write a function whose arguments are two strings. The function
#should return the sum of these strings modulo 10. This function has
#a small pitfall. In order to perform addition modulo 10 symbols must
#be converted into numbers by the int() operation and, in otder to add
#a digit to the new string it should be converted back into a symbol
#by the str() operation.
#(c) Write a program whose input is a list of strings of the same length
#whose symbols are digits. The program should go through all pairs
#of these strings (without repetition) and print their sums modulo 10.


def main():

    result1 = calcModTen(7,8)
    print(result1)


    result2 = mod4Strings('928','135')
    print(result2)

    
    J = ['0345','7896','6543','7812']
    result3 = mod4List(J)
    print(result3)

    

def calcModTen(a,b):
    if(a+b < 10):
        modTen =  a+ b
    else:

        modTen =  a+ b -10
    return modTen



def mod4Strings(A,B):
    myStr=''
    for i in range (len(A)):
        result = calcModTen(int(A[i]), int(B[i]))
        myStr = myStr + str(result)
    return  myStr

def mod4List(A):
    
    for i in range (len(A)-1):
        
        result = calcModTen(int(A[i]), int(A[i+1]))
        myStr =  str(result)
        print(myStr)


main()
        
