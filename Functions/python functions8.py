#Let Str1 and Str2 be two strings of the same length.
#The strings differ in position i if Str1[i] does not equal Str2[i].
#For instance the strings "abcde" and "bbfde" differ in positions 0 and 2.
#The Hamming distance between two strings of the same length is the number
#of positions in which they differ. 
#Write a function whose arguments are two strings of the same length and that returns their Hamming distance.



def main():
    check = hammingDistance('abcde', 'bbfde')
    print(check)

    myList_1 = ['abcde','bbfde','bbfde','asdae','abcde']
    check2 =hammingDistanceList(myList_1, 'bbfde')
    print(check2)
    
    

def hammingDistance(word_1, word_2):
    hammingD = 0
    ham=0
    for i in range(len(word_1)):
        if (word_1[i] != word_2[i]):
    
           hammingD =  hammingD + 1

    return hammingD 

            
   
#Use this function for a program whose input is a list A of strings and an additional 
#string Str. The program should print the largest Hamming distance between Str and an element of A.


def hammingDistanceList(myList, word_3):
    myhammingDList=[]
    for i in range (len(myList)):
        hammingDl = hammingDistance(myList[i], word_3)
        myhammingDList.append(hammingDl)

    maxHammingDistance= max(myhammingDList)
    return maxHammingDistance

main()
