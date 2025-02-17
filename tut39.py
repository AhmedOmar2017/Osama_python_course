#---------------------------------------
#--------- slice E mail ----------------
#---------------------------------------


TheName = input("Your name\'s?").strip().capitalize()
TheEmail = input("Your Email\'s?").strip()
theUserName = TheEmail[:TheEmail.index("@")]
TheWebsite = TheEmail[TheEmail.index("@")+1:]

print(f" Hello {TheName} your email is {TheEmail}")
print(f"your user name is {theUserName}\nyour web site {TheWebsite}")