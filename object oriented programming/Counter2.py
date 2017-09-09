##Write a function called click that accepts a numeric value and returns that value plus one.
##Write a function called reset that does not have any arguments and returns zero.
##Add an additional method to the Class Counter that can undo a click. Make sure that the undo
##method cannot be used more often than the click() method.

##Simulate a tally counter that can be used to admit a limited number of people. First the limit is set
##with a call:
##def setLimit(self, maximum)
##If the count reaches the limit, simulate an alarm by printing out a message “Limit Exceeded”

class Counter:
    def __init__(self):
         self.number=0
         self.Limit=0



    def click(self):
        if (self.number > self.Limit):
            print('Limit exceeded, currently:   ' + str(self.number))
            
        else:
            
            self.number =self.number + 1
        
    def reset(self):
        self.number  == 0

    def unDoClick(self):
        if(self.number > 0):
            self.number =self.number - 1

    def setLimit(self,maximum):
        self.Limit= maximum
        
    def getCount(self):
        if (self.number > self.Limit):
            print('Limit exceeded, currently:   ' + str(self.number))
        else:
            print(self.number)


            
        
    
myCounter= Counter()
myCounter.setLimit(6)
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.getCount()

