#---------------------------------------------------------------------------
#--- Practical => Loop on my Iterators with zip() --------------------------
#---------------------------------------------------------------------------

# zip() Return A zip object contain all objects
# zip() length is length of lowest object
#------------------------------------------------


list1 = [1,2,3,4,5]
list2 = ["A","B"]
list3 = ["A","B", "C", "D"]
tuple1 = ("Man", "woman", "Girl", "boy")
Dictionary = {"name": "Ahmed", "Age": 36, "country": "Egypt"}

ultimatelist = zip(list1,list2)

print(ultimatelist)


for item in ultimatelist:
    print(item)

print("#" * 40)

for item in zip(list1,list3):
    print(item)


print("#" * 40)

for item1, item2, item3, item4 in zip(list1,list3, tuple1, Dictionary):
    print("List 1 item =>", item1)
    print("List 2 item =>", item2)
    print("Tuple 3 item =>", item3)
    print("Dict 1 key =>", item4, "value =>" ,Dictionary[item4])

print("#" * 40)