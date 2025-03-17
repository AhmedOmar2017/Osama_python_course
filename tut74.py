#--------------------------------
#-- Built in Function => --------
#--------------------------------

# [1] Reduce Take A function + iterator
# [2] Reduce run A function on first and second element and give result
# [3] Then Run function on Result  and third element
# [4] Then Run function on Result  and fourth element and so on
# [5] Till One element is left and This is The Result of The Reduce
# [6] The function Can be pre-defined function or Lambda Function
#---------------------------------------------------------------------

from functools import reduce

def sumall (nam1,num2):
    return nam1+num2

numbers = [1,2,3,4,5,56,7]

result = reduce (sumall, numbers)
print(result)



result2 = reduce (lambda nam1,num2: nam1+num2, numbers)
print(result2)