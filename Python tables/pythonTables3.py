#Write a program whose input is a table with integer elements. The program
#Write a program whose input is a table with integer elements. The program
#should print “YES” if in each column the elements are all different and “NO”
#otherwise. Apply function of task 1 to obtain the transpose of the input matrix. The
#use your solution for task 2.



def main():

    A= [
        [1,2,3,4],
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
