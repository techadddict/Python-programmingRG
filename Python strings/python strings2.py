

def main():

    mynumber = int(input('Enter a number'))

    check = checkNum (mynumber)

    print(check)

    myListT= [4,15,12,7,9,18,11]

    checkMyList = checkList(myListT)

    print(checkMyList)
    
    

#write a function that returns 1 if a number is between 10 and 20 and 0 otherwise.
def checkNum (number):
     if(10 < number and number < 20):
        return 1

     else:
        return 0

#Write a program whose input is a list and that uses the above  function to count the number of
#elements between 10 and 20 in the list.
    

def checkList(myList):
    countNum=0
    for i in range(len(myList)):
        if(checkNum (myList[i])==1 ):
            countNum = countNum + 1
    return countNum
        
        
main()
             
             






