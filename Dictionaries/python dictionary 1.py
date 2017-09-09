##Write a program that counts how often each word occurs in a user specified text file

file = open('text.txt','r')
lines= file.readlines()
myDict={}
for line in lines:
       #print(line)
      wordList = line.strip().split()
      for word in wordList:
          word=word.strip(',!;.')
          if(word in myDict):
              #if words are many 
             myDict[word]=myDict[word] +1
   
          else:
                
                #if word is the only one 
             myDict[word] = 1
#file.close()
for word in myDict:
    print(word,myDict[word])
