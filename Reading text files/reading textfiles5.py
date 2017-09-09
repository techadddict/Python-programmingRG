#Read two country data files, worldpop.txt and worldarea.txt. These files can be found on
#Write a file world_pop_density.txt that contains country names and population densities with the
#country names aligned left and the numbers aligned right.

popData =open ( 'worldpop.txt','r')
areaData =open ( 'worldarea.txt','r')
popLines= popData.readlines()
areaLines = areaData.readlines()
worldPopDen = open ( 'worldPopDensity.txt','w')


for i in range(len(popLines)):
    country= (''.join(list(filter(str.isidentifier, popLines[i]))))
    population=int(''.join(list(filter(str.isdigit, popLines[i]))))
    area=int(''.join(list(filter(str.isdigit, areaLines[i]))))
    if(area>0):
       popDen= population/area
       worldPopDen. write( country + '    ' + str(popDen))
    else:
        popDen= 0
        worldPopDen. write( country + '    ' + str(popDen))
    
