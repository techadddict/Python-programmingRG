#1.3. Let us say that a list A is *sorted* if its elements are stored
#in the ascending order. For instance, A=[1,3,3,4,8,12] is sorted
#while A=[8,10,1,14,16]  is not because 10>1. 
#Please write a program whose input is a list A and whose output
#is `sorted' if A is sorted and `not sorted' otherwise.


number = int (input('how many elements would you like to enter in your list'))

myList=[]
for i in range (0, number):
    element=int(input('enter a number'))
    myList.append(element)



myList.sort()

print(myList[1])
