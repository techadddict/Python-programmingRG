#Write a program that counts the number of lines in a text file
filename ='lyricso.txt'  #use filename of your choice
file =open (filename ,'r')
lines=file.readlines()
print(len(lines))
