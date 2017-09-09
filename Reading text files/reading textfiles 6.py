#Read two country data files, worldpop.txt and worldarea.txt. These files can be found on
#Write a file world_pop_density.txt that contains country names and population densities with the
#country names aligned left and the numbers aligned right.

#assumes all countries are in the files
popData =open ( 'worldpop.txt','r')
areaData =open ( 'worldarea.txt','r')
popLines= popData.readlines()
areaLines = areaData.readlines()
worldPopDen = open ( 'worldPopDensityr.txt','w')


for i in range(len(popLines)):
    countryPolLines= (''.join(list(filter(str.isidentifier, popLines[i]))))
    population=int(''.join(list(filter(str.isdigit, popLines[i]))))
    area=int(''.join(list(filter(str.isdigit, areaLines[i]))))
    countryAreaLines=(''.join(list(filter(str.isidentifier, areaLines[i]))))
    if(area > 0 ):
       popDen= (population/area)
       popDen = round(popDen,2)
       worldPopDen. write( countryPolLines + '    ' + str(popDen) + '\n')

    else:
       popDen= 0
       
       worldPopDen. write( countryPolLines + '    ' + str(popDen) + '\n')
    
        
    
worldPopDen.close()

file= open ( 'worldPopDensityr.txt','r')
lines = file.readlines()
for line in lines:
    print(line)
