
#Write a function whose argument is a string.
#The function should return 1 if the string is a palindorme and 0 otherwise.



def main():
    check = isPalidrome('abcba')
    #print(check)

    
    myList=['jjjjj','abcba','hhjjn','bbdlb','klmlk']

    check2 = isPalidromeList(myList)
    print(check2)

    

def isPalidrome(word):
    isPal=1
    for i in range(len(word)):
        if (word[i] != word[len(word)-1-i]):
             isPal=0
            
        

    if ( isPal==0):
        
       return 0
    else:

       return 1


#Use this function in a program whose input is a list of strings.
#The program prints the number of elements in the list that are palindromes.

def isPalidromeList(words):

    countP= 0
    for i in range (len(words)):

        if( isPalidrome(words[i]) == 1 ):
            countP  =  countP + 1
    return countP
            
        


       


main()
