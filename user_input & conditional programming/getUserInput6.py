#A string Str1 is a *prefix* of a string Str2 if Str2 can be obtained by adding symbols
#to the right of Str1. For instance the string `abbc' is a prefix of the string `abbcadd' and not a prefix
#of the string `abbdab'. Symmetrically, Str1 is a *suffix* of a string Str2 if Str2 can be obtained by adding 
#symbols to the left of Str1. For instance `abbc' is a suffix of `adbabbc' and not a suffix of `ddbbc'.
#Write a program that requests from the user two strings and tells the user whether the second string
#is a prefix of the first one, a suffix of the first one or neither of them. 

myStr1=input('Enter a  string')
myStr2=input('Enter a string')

len1=len(myStr1)
len2=len(myStr2)
isPrexix=0
for i in range(0,len1):
    if ( myStr1 == myStr2[0:len1]):
        isPrexix=1
        break
    

if ( isPrexix==1):
   print(myStr1 + ' is a prefix of '+ myStr2)
else:

   print(myStr1 + ' is not a prefix of '+ myStr2)
    


myStr1=input('Enter a  string')
myStr2=input('Enter a string')

len1=len(myStr1)
len2=len(myStr2)
isSuffix=0
for i in range(0,len1):
    if ( myStr1 == myStr2[len1-1:]):
       isSuffix=1
       break
    

if (isSuffix==1):
   print(myStr1 + ' is a Suffix of '+ myStr2)
else:

   print(myStr1 + ' is not a Suffix of '+ myStr2)
