#Let us call a number GOOD if it is great than or equal to 40 and
#smaller than 50 (that is 40,41,...,49).
#Write a program that asks the user to enter a number and then prints
#GOOD if the number is good and
#BAD otherwise


#The program should use nested IFs:

number = int(input('Please enter a number'))

if (number > 39):
    if(number < 50):
       print('GOOD')

    else :
        print('BAD')
else:
    print('BAD') 
        
            
#Then write a program solving the same task but using a logical connective (AND or OR). 

number = int(input('Please enter a number'))

if (number > 39 and number < 50):
       print('GOOD')

else :
       print('BAD')
