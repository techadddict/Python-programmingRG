# UZXVK undergraduate modules are classified by 
#   their level and the number of credits.
#  In particular, there may be modules of levels 4,5,6 and modules
#   having 15 or 30 credits.
#   The *weight* of a module is computed  as follows.
#   -The weight of any level 4 module is 0.
#   -The weight of a level 5 module worth 15 credits is 1.
#   -The weight of a level 5 module worth 30 credits is 2.
#   -The weihgt of a level 6 module worth 15 credits is 2.
#   -The weight of a level 6 module worth 30 credits is 4.

#  Suppose the mark of a student for a module is X.
#  Then the weighted mark for the module is X multiplied by the module weight.

#  a) Write a function whose arguments are: module mark, the number of credit for the module,
#    and module level. The function should return the module weight and the weighted mark.
#    (Note that the specified function returns two values)

#  b) Write a program whose input are three lists Marks,Levels, and Credits, all of the same length.
#     They represent marks, level, and credits for modules numbered 0,...,len(Marks)-1.
#     (The names of the modules are not important for this exercise).
#     In particular, Marks[i], Levels[i], and Credits[i] are respective marks, level, and credit for
#     module number i.
#     Please feel free to assume that the data in the list is valid i.e. that all the elements in the Marks
#     list are between 0 and 100, all the elements in the Levels list are 4,5, or 6, and all the elements in
#     the Credits list are 15 or 30.  Moreover, you can create these lists fixed in the program instead
#     of asking the user to enter them.

#     Your program should do the following.
#     i) Calculate the total number of credits for the modules whose marks are 40 or more
#        (40 is the lowest passing mark for our undergraduate students).
#     ii) Calculate the total number of credits for the modules whose marks are 40 or more
#         and whose level is 6.

#     iii) If the result of i) is at least 360 *and* the result of ii) is at least 120 then
#          Compute the sum SW of all module weights and the sum SM of all weighted marks for modules as per i)
#          Obtain the weighted average mark AV=SM/SW.
#          Print "The student graduates with average", AV.
     
#          Otherwise (if the condition in the beginning of this item is not true),
#          print: "The students is not ready to graduate". 

#     You should use the function in 3a) for this program.

def main():

    myweightedMark = calC_weightedMark(67, 15,6)
    print(myweightedMark)

def calC_weightedMark(module_Mark, no_Of_Credit,module_Level):
    
    if(module_Level == 4):
       weight = 0
    if(module_Level == 5 and no_Of_Credit ==15):
        weight = 1
    if(module_Level == 5 and no_Of_Credit ==30):
       weight = 2
    if(module_Level == 6 and no_Of_Credit ==15):
       weight = 2
    if(module_Level == 6 and no_Of_Credit ==30):
       weight = 2

    weighted_Mark= weight * module_Mark

    return ('The module weight is '+ str(weight) + ' and the weighted mark is '+ str(weighted_Mark) )
    


main()
