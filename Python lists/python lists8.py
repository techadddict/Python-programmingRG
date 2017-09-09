#3.1. Please write a program whose input is a string S. The program should treat S as a sequence of numbers
#separated by non-digit symbols. The output of the program are the numbers extracted from S.
#For instance if S="fg123ab34fff45cv576" then the numbers printed should be
#123
#34
#45
#576


S="fg123ab34ff9f45cv576gb7"
for i in range (len(S)-2):
    if(S[i].isdigit() and S[i+1].isdigit() and S[i+2].isdigit()):
        print(S[i]+S[i+1]+S[i+2])

    if(S[i].isdigit() and S[i+1].isdigit() and not( S[i+2].isdigit()) and not (S[i-1].isdigit())):
        print(S[i]+S[i+1])

    if(S[i].isdigit() and not(S[i-1].isdigit()) and not ( S[i+1].isdigit())):
       
       print(S[i])

    if(S[len(S)-1].isdigit() and  (not(S[len(S)-2].isdigit()))):
       
       print(S[len(S)-1])
       break
