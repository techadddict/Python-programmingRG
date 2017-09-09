#Program will first ask the user the number of numbers the user intends to enter. After that the program will request from the user to enter
#*that* number of numbers and compute the sum of even and odd numbers among them.



numberOfElements =int(input('How many numbers would you like to enter'))
sum_EvenNumber = 0
sum_OddNumber  = 0
for i in range (0, numberOfElements):
    number = int(input('PLease enter a number'))
    if (number% 2 ==0):
        sum_EvenNumber = sum_EvenNumber + number

    if( number % 2 ==1 ):
        sum_OddNumber = sum_OddNumber + number

print(sum_EvenNumber)
print(sum_OddNumber)

