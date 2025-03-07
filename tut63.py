#--------------------------------
#--------function recursion -----
#-- to understand recursion you ned first understand recursion --
#----------------------------------------------------------------


def cleanWord (word):
    if len(word) == 1:
        return word
    print(f"Before function start {word}")
    if word[0] == word[1]:
        print(f"Before condition  {word}")
        return cleanWord(word[1:])
    print(f"after condition  {word}")
    return word[0] + cleanWord(word[1:])
print(cleanWord("wwwwoooorrldd"))