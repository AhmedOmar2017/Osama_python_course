# -----------------------------------------
# ---- Iteraable VS Iterator --------------
# -----------------------------------------
#
# Iterable
# [1] Object contains data that can be iterated Upon
# [2] Examples (String, List, set, Tuple, Dictionary)
# ----------------------------------------------------
# Iterator
# [1] Object used to Iterate over Iterable Using next() method Return 1 Element at A time
# [2] You Can Genenrate Iterator from Iterable when using iter() method
# [3] For loop Already call iter() method on the iterable behind the scene
# [4] Gives "stopiteration" if theres on next element
# -------------------------------------------------------------------------------------------

MyName = "Ahmed"
myList = [1, 3, 45, 6, 7, 8]

for letter in MyName:
    print(letter, end=" ")

for N in myList:
    print(N, end=" ")


myIterable = iter(MyName)

print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
#print(next(myIterable))  stop iteration

for L in iter("Ahmed"):
    print(L, end= " ")


