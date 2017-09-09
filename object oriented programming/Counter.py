class Counter:
    def __init__(self):
        self._value=0
        self._Limit=0 


    def reset (self):
        self._value= 0
        
      
    def setLimit(self,maximum):
        self._Limit=maximum
        

    def click(self):
        self._value= self._value + 1
        if(self._value > self._Limit):
           print("Limit exceeded")
           

    def undo(self):
       if(self._value > 0):
           self._value=self._value - 1
          
    def getValue(self):
        return (self._value)
     

myCounter=Counter()
myCounter.reset()
myCounter.setLimit(5)
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.click()
myCounter.click()
