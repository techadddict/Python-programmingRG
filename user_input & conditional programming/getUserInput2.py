

#Exercise 2. Modify your program for Exercise 1  so that it will print the number of even numbers entered and the number
#of odd numbers entered. In the above example, the number of even numbers is 3 and the number of odd numbers is 2



number = int(input ('Enter a number and 0 to end program'))
count_EvenNumbers=0
count_OddNumbers=0
while (number != 0):
       if( number % 2 == 0):
           count_EvenNumbers= count_EvenNumbers + 1

       if( number % 2 == 1):
           
         count_OddNumbers= count_OddNumbers + 1

      
       number = int(input ('Enter a number and 0 to end program'))

print(count_EvenNumbers)
print(count_OddNumbers)
      
