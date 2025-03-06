#--------------------------------------
#-- Function default parameter --------
#--------------------------------------

# you set value if you miss values it will add automatically
# It must be the last argument if it only one

def say_hello (name, age, country = "Unknown"):
    print(f"Hello {name} your age is {age}, and your country is {country}")



say_hello("Ahmed", 31, "Egypt")
say_hello("omar", 50)