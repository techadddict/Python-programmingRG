##Re-implement the CashRegister class so that it keeps track of each added item in the list.
##Remove the _itemCount and _totalPrice instance variables. Re-implement the clear,
##addItem, getTotal and getCount methods. Add a method displayAll that displays the
##prices of all items in the current sale

class CashREgister:
     def __init__(self):
         self.itemList=[]



     def addItem(self,item):
         self.itemList.append(item)


     def getCount(self):
         count= len(self.itemList)
         
         return count

     def getTotal(self):
         sumList= sum(self.itemList)
         
         return sumList

     def displayAll(self):
         for i in self.itemList:
             print(i)

     def clearList(self):
         self.itemList=[]
         


myCashREgister=CashREgister()
myCashREgister.addItem(5.78)
myCashREgister.addItem(3.00)
myCashREgister.addItem(1.20)
myCashREgister.addItem(2.20)
myCashREgister.addItem(0.99)
print(myCashREgister.getCount())
print(myCashREgister.getTotal())
myCashREgister.displayAll()
myCashREgister.clearList()
print(myCashREgister.getCount())
print(myCashREgister.getTotal())




