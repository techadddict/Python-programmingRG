#Please write a program whose input is a string which is an arithmetical expression with operations `+' and `-'
#and without brackets. The program should evaluate the expression and print the result of the evaluation.
#For instance if S="5+8-7-5+1" then the output should be 2.



result=0
S="5+8-7-5+1"
#    for i in range(len(S)-1):        
print(eval(S))

for i in range(len(S)-1):
    if(S[i].isdigit()):
        result= result + int(S[i])

    else:
        if(S[i]=='+'):
           result= result + int( S[i+1])

        if(S[i]=='-'):
           result= result - int(S[i+1])
            


print(result)        
    
        
        
   
   
