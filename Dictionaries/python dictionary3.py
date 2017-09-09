#Write a program that reads in two files and prints out, in sorted order, all words that are common to
#both of them.

#use intersection for 2 sets
def main():
    mySet1=getWords('words.txt')
    mySet2=getWords('text.txt')

    mySet3= mySet1.intersection(mySet2)

    for item in mySet3:
        print(item)
    

def getWords(file):
    mySet=set()
    file = open(file,'r')
    line = file.readline()
    for line in file:
        wordList= line.rstrip().strip(',.;!').split()
        for word in wordList:
             mySet.add(word)
    return mySet


main()
