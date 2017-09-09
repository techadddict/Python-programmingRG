# This program requests from the user to enter an integer number until the user enters a zero.
#Then the program prints the sum of even numbers entered and the sum of odd numbers entered.

num_liste=[]

n=int(input('enter a number or 0 to stop the sequence'))
while (n != 0):
     num_liste.append(n)
     
     n=int(input('enter a number or 0 to stop the sequence'))
    
sumEven=0
sumOdd=0
for i in range (len(num_liste)):
    if (num_liste[i] % 2 == 0):
        sumEven = sumEven + num_liste[i]
        
    if (num_liste[i] % 2 == 1):
        sumOdd = sumOdd+ num_liste[i]
print(sumEven)
print(sumOdd)
         


