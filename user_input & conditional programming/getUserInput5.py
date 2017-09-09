# A *palindrome* is a string that reads the same from the left to the right and from the right
#to the left. For instance, the string `abbba' is a palindrome while the string `abbbd' is not 
#(the latter string will read `dbbba' from the right to the left). Write a program that requests from the
#user a string and tells the user whether this string is a palindrome.

myStr = input('Enter a word to test if its a palindrome')
isPalidrome =True
for i in range(len(myStr)):
    if (myStr[i] != myStr[len(myStr) -1 -i]):
        isPalidrome =False
        break

if (isPalidrome ==True):
    
    print ( myStr + ' is a palidrome')


else:

    print ( myStr + ' is  not a palidrome')
         
