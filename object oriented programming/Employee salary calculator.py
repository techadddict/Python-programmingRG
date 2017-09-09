class Employee:
    def __init__(self):
        self._salaryPerHour=0
        self._weeklyWorkHours=0 

      
    def setSalaryPerHour(self,salary):
        if(salary > 0):
             self._salaryPerHour = self._salaryPerHour + salary
             return True
        return False
        
      
    def setWeeklyWorkHours(self,numHours):
        if(numHours>0):
            self._weeklyWorkHours =self._weeklyWorkHours + numHours
            return True
        return False

    def getWeeklyWorkHours(self):
        return self._weeklyWorkHours



    def getSalaryPerHour(self):
        return self._salaryPerHour
        
    def calculateWeeklyPay(self):
        return self.getSalaryPerHour() * self.getWeeklyWorkHours()
        
    def __repr__(self):
        return  'weekly pay  ='  +  str(self.calculateWeeklyPay())

class FixedTermEmployee(Employee):
    
    def __init__(self, numHours=40):
       super(). __init__()
       self._weeklyWorkHours=numHours
       self._salaryPerHour=0
       
    def setSalaryPerHour(self,salary):
        super().setSalaryPerHour(salary)
        
      
    def setWeeklyWorkHours(self,numHours):
        if(numHours!=40):
            self._weeklyWorkHours =40
            return False
        else:
            self._weeklyWorkHours =40
            return False

    def getWeeklyWorkHours(self):
        return self._weeklyWorkHours


    def getSalaryPerHour(self):
        return  super().getSalaryPerHour()
        
    def calculateWeeklyPay(self):
        return super().calculateWeeklyPay()
        
    def __repr__(self):
        return  'weekly pay  = '  +  str(self.calculateWeeklyPay())

       
    
myEmployee=Employee()
print(myEmployee)
print(myEmployee.setWeeklyWorkHours(20))
print(myEmployee.setSalaryPerHour(10))
print(myEmployee)
print(myEmployee.setSalaryPerHour(-10))
print(myEmployee)




    
myFixedTermEmployee=FixedTermEmployee()
print(myFixedTermEmployee.getWeeklyWorkHours())
print(myFixedTermEmployee.setWeeklyWorkHours(20))
print(myFixedTermEmployee.getWeeklyWorkHours())
print(myFixedTermEmployee.setSalaryPerHour(10))
print(myFixedTermEmployee)
