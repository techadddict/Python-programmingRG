#This code gets list from unser and prints the items in the list.

n=int(input('How many items would you like to enter'))
new_List=[]
for i in range (0,n):
    number =input('Enter an item')
    new_List.append(number)


for i in new_List:
    print(i)

