file =open ('hello.txt','w')
file.write('checking if works')
file.close()
file =open ('hello.txt','r')
line=file.readline()
while line != '':
      print(line)
      line=file.readline()
      
    
