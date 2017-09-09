# suppose now that the number is good if it is smaller than 20 or
#larger than 80. Write a program that asks the user to enter a number and then prints
#GOOD if the number is good and
#BAD otherwise


#Then write a program solving the same task but using a logical connective (AND or OR):

number = int(input('Please enter a number'))

if (number < 20 or number >80):
    print('GOOD')
else:

    print('BAD')

