#Write a program that asks the user for a file name and prints the number of characters, words and lines in
#that file

filename = input('Please enter a filename to open')
#filename ='lyricso.txt'  #use filename of your choice
file =open (filename ,'r')
lines=file.readlines()
lettersCount=0
wordsCount= 0
for line in lines:
    words=line.strip('/*,!./').strip(.rstrip().split()
    lettersCount = lettersCount + len(line)
    wordsCount = wordsCount + len(words)
    
numLines =len(lines) 

print(numLines)
print(lettersCount)
print(wordsCount)
