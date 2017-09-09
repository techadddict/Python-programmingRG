class Person():                                                                                                                                                                                     
   def __init__(self,name,year):                                                                                                                                                                    
         self._name=name                                                                                                                                                                              
         self._year=year    
         
   def __repr__(self):
        return 'my name is ' + self._name + ' and I was on in '+ str(self._year)
                                                                                                                                                                                                       
                                                                                                                                                                                                            
class Student(Person):                                                                                                                                                                              
   def __init__(self,name,year,course):                                                                                                                                                            
         super().__init__(name, year)                                                                                                                                                                   
         self._course=course   
           
   def __repr__(self):
       return  'my name is ' + self._name + ' and I was born in ' + str(self._year)+ ' and am studying '+ self._course
                                                                                                                                                                                                            
class Instructor(Person):                                                                                                                                                                         
   def __init__(self,name,year,salary):                                                                                                                                                          
         super().__init__(name,year)                                                                                                                                                             
         self._salary=salary 
         
   def __repr__(self):
       return "my name is "+ self._name + " I was born in "+str(self._year)+ ' and I earn  '  +str(self._salary) + ' pounds per month'
                                              
                                         
                                         
                                         
myperson=Person("hanna",1945)
mystudent=Student("Christian", 1716,"history")
myinstructor=Instructor("Martin",90,478)
print(myperson)
print(mystudent)
print(myinstructor)

