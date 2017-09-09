

##Write a program that requests from the user to enter an integer number until the user enters a zero.
#Then the program prints the sum of even numbers entered and the sum of odd numbers entered.
#For instance if the user enters 5 10 5 10 0 then the sum of even numbers is 20 and the sum of odd numbers
#is 10.


number = int(input ('Enter a number and 0 to end program'))
sum_EvenNumbers=0
sum_OddNumbers=0
while (number != 0):
       if( number % 2 == 0):
           sum_EvenNumbers= sum_EvenNumbers + number

       if( number % 2 == 1):
           
         sum_OddNumbers= sum_OddNumbers + number

      
       number = int(input ('Enter a number and 0 to end program'))

print(sum_EvenNumbers)
print(sum_OddNumbers)
      
