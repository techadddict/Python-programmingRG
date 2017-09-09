#Please write a program whose input is a list A and whose output
#is an index of the smallest element of A. For instance if A=[8,4,3,6,9,9]
#the output should be 2. Notice that `an index' used rather than `the index'.
#This is because of possible multiple occurrences of the smallest element.
#For instance if A=[3,8,3,6,5] then both 0 and 2 are correct outputs.
#For instance you can choose to print the index of the first occurrence
#of the smallest element.

number = int (input('how many elements would you like to enter in your list'))

myList=[]
for i in range (0, number):
    element=int(input('enter a number'))
    myList.append(element)


minimumElement= min(myList)
print(myList.index(minimumElement))


              
