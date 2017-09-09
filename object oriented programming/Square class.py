class Box:
    def __init__(self,width,depth,height):
        self._width=width
        self._depth=depth
        self._height=height
        
    def getWidth(self):
        return self._width
        
    def getDepth(self):
        return self._depth
        
    def getHeight(self):
        return self._height
        
        
        
class Square(Box):
    def __init__(self,width,height):
        super().__init__(width,width,height)
        self._width=width
        self._height=height
       
        
        
    def getWidth(self):
        return self._width
        
    def getDepth(self):
        return self._width
        
    def getHeight(self):
        return self._height
        
        
        
b = Box(3,4,5)
vol = b.getWidth() * b.getDepth()* b.getHeight()
print("volume =",vol)
print('expected 60')
print(b)        
sq=  Square(4,7)

print (sq.getDepth())
print('expected 4')
print(sq.getWidth())
print('expected 4')
print(sq.getHeight())
print('expected 7')
