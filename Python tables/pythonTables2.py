#Write a program whose input is a table with integer elements. The program
#should print “YES” if in each row the elements are all different and “NO”
#otherwise.
#Hint: Write a function whose argument is a list and which returns 1 if the
#elements of this list are all different and 0 otherwise. Then apply this function
#to each row of the input table


def main():

    A= [
        [1,3,3,4],
        [22,15,33,45],
        [0,0,1,1],
        [1,1,2,2]
       ]

    result = checkElements(A)
    
    
def checkElements(A):
    
    found=0
    count = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if(A[i].count(A[i][j]) > 1 ):
              found=1
          
    if(found ==1 ):
        print('No')
        

    else:
        print('Yes')
        
      


main()
