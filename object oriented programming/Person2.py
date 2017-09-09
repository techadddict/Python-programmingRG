##Implement a superclass called Person. Make two classes, Student and Instructor,
##that inherit from Person. A person has a name and a year of birth. A student has a course
##and an instructor has a salary. Write the class declarations, the constructors and the
##__repr__ method for all classes. Supply a test program that tests these classes and
##methods.

class Person:
    def __init__(self,name,year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    def __repr__(self):

        return  'My name is  '+ self.name + ' and I am a person born in  '+ str( self.year_of_birth)

class Student(Person):
      def __init__(self,name,year_of_birth,course):
          super().__init__(name,year_of_birth)
          self.course = course

      def __repr__(self):

        return  'My name is  ' + self.name + ' and I am a student born in  '+ str( self.year_of_birth) + ' and I am studying '+ self.course


        


class Instructor(Person):
      def __init__(self,name,year_of_birth,salary):
          super().__init__(name,year_of_birth)
          self.salary = salary

      def __repr__(self):

        return 'My name is  ' +self.name + ' and I am an Instructor  born in  '+ str( self.year_of_birth) + ' and I earn $%.2f ' %self.salary +'salary'

          
    
      
myPerson= Person('Hanna',2016)
print(myPerson)
myStudent= Student('Christian',2013,'Python Programming')
print(myStudent)
myInstructor= Instructor('Martin',1980,10000)
print(myInstructor)
