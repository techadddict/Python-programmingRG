# writing a function that takes two integer numbers a and b and returns a//b and a%b
def main():

    answer2 = division (7,3)

    print(answer2)

def division(a,b):
    
    floorDivision = int(a)  //  int(b)

    remainder = int(a)  %  int(b)
        
    return ('Floor division of ' + str(a) + ' and  ' + str(b) + '  =  ' + str(floorDivision),
            'The remainder after dividing  '+ str(a) + ' and  ' + str(b) + '  =  ' + str(remainder) )



main()
