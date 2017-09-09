#write a function that receives a string and returns this string doubled.
def main():

    answer = doubleString('work')

   # print(answer)

def doubleString(word):
    dString = word + word
    return dString



main()
#Then write a program whose input is a string. The program should go through the input
#string and form a new one where each symbol is replaced by its double (using the above function).
#if we we enter "abcd", the program should print "aabbccdd"


def main():

    answer2 = doubleEachLetter ('abcd')

    print(answer2)

def doubleEachLetter(word):
    
    newString=''
    for i in range (len(word)):
        newString  =  newString  + (word[i]+word[i])
        
        
    return newString



main()

