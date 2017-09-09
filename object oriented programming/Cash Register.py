class CashRegister:

      def  __init__(self):
          self._itemList=[]

      def addItem(self,price):
          self._itemList.append(price)

      def clearList(self):
          self._itemList=[]

      def getTotal(self):
          return sum(self._itemList)

      def getCount(self):
          return len(self._itemList)

      def displayAll(self):
          print('Your basket has the following items:' +  str(self.getCount()) + '  totalling ' + str( self.getTotal()) + ' pounds')
          for i in range(len(self._itemList)):
              print(float(self._itemList[i]))

myCashRegister=CashRegister()
myCashRegister.addItem(1.25)
myCashRegister.addItem(0.66)
myCashRegister.addItem(9.57)
myCashRegister.addItem(1.00)

print(myCashRegister.getTotal() )
print(myCashRegister.getCount() )
myCashRegister.displayAll()

