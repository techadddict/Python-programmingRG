#Write a program reads a file containing text. Read each line and send it to the output file, preceded by line
#numbers. If the input file is:
#Mary had a little lamb
#Whose fleece was white as snow.
#And everywhere that Mary went,
#The lamb was sure to go!
#Then the program produces the output file:
#/* 1 */ Mary had a little lamb
#/* 2 */ Whose fleece was white as snow.
#/* 3 */ And everywhere that Mary went,
#/* 4 */ The lamb was sure to go!


infile =open ('lyrics.txt','r')
outfile =open ('lyricso.txt','w')

lines=infile.readlines()
for i in range(len(lines)):
    outfile.write('/*'+ str( i+1) +  '*/' + '  ' + lines[i])
infile.close()
outfile.close()
file =open ('lyricso.txt','r')
line=file.readline()
while line != '':
      print(line)
      line=file.readline()
      
