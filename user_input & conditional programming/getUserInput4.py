#Write a program that requests from the user to enter a string MyStr and a symbol symb. 
#The program then prints the number of times symb occurs in MyStr.
#For example, symbol `b' occurs 3 times in the string `abbcddba'

symb= input('Enter a symbol/character/letter')
myStr = input('Please enter a word')
print(myStr.count(symb))
