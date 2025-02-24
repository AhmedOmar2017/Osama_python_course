#--------------------------------------
#------- Loop while training ----------
#--------------------------------------
MyF = ["AD", "qw", "df", "wt", "Gh", "we"]

a = 0
while a < len(MyF):
    print(f" #{str(a +1).zfill(2)} {MyF[a]} ")
    a += 1
else:
    print(" All friends are printed")
