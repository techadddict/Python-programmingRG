number = int (input('how many elements would you like to enter in your list'))

myList=[]
for i in range (0, number):
    element=int(input('enter a number'))
    myList.append(element)


sortedL =1
for i in range(len(myList)-1):
    if(myList[i] > myList[i +1]):
        sortedL = 0
        break
if(sortedL == 0):
    print('The list is not sorted')
else:
    print('The list is sorted')
    

