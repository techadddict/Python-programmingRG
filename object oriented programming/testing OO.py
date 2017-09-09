class TestO:
    def  __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.t=0
        
    def add(self,k):
        self.x=self.x + k

    def subtract(self,t):
         self.y=self.x -t

    def squarevalue(self,g):
        self.z=g*g

    def multiply(self,m,n):
        self.t=m*n

    def get_add_R(self):
        return self.x

    
    def get_subtract_R(self):
         return self.y

    def get_squarevalue_R(self):
         return self.z


    def get_multiply_R(self):
         return self.t


myTestO=TestO()
myTestO.add(6)
myTestO.add(5)
print(myTestO.get_add_R())
print('expected 11')
myTestO.subtract(3)

print(myTestO.get_subtract_R())
print('expected 8')
myTestO.multiply(10,7)
print(myTestO.get_multiply_R())
print('expected 70')



    
        
        
    
        
     
         
        
        
