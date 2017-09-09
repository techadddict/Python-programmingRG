#Create a class MultiChoiceQuestion that inherits from the Question class. This class
#callows for multiple correct choices. The respondent should provide all correct choices,
#cseparated by spaces. 
class Question:


    def __init__(self):
        self.questionAnswer= ''
        self.response=''
        
    def setQuestion(self,question):
        self.response=input(question)
         
    def setAnswer(self,answer):
         self.questionAnswer = answer
 

    def checkAnswer(self):
         if(self.questionAnswer == self.response):
             print('Thats correct, well done!')
         else:
              print('Thats false,better luck next time!')


class MultipleChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self.AnswerList=[]
        self.ResponseList=[]

        
    def setQuestion(self,question):
        self.response=input(question)
        self.response = self.response.strip(',.''').rstrip().split()
        self.ResponseList=self.response
         
    def setAnswer(self,answer):
        self.questionAnswer = answer
        self.questionAnswer=self.questionAnswer.strip(',.').rstrip().split()
        self.AnswerList=self.questionAnswer
        
        
 

    def checkAnswer(self):
         if(self.AnswerList.sort() == self.ResponseList.sort()):
             print('Thats correct, well done!')
         else:
              print('Thats false,better luck next time!')
            


myQuestion =  Question ()
myQuestion.setQuestion('Who is the PM of the uk')
myQuestion.setAnswer('Theresa May')
myQuestion.checkAnswer()

myMultipleChoiceQuestion = MultipleChoiceQuestion()
myMultipleChoiceQuestion.setAnswer('apple,banana,pear')
myMultipleChoiceQuestion.setQuestion('My favourite fruits are:')
myMultipleChoiceQuestion.checkAnswer()


             
         
         
