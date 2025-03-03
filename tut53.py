#-----------------------------
#-----------nested for loop --
#-----------------------------


#  for skill in skills: #inner loop
 #       print(f" - {skill}")


people = {
    "Ahmed" : {
        "c": "100%",
        "cpp" : "30%",
        "c#"  : "10%"
    },

        "Omar": {
            "c": "40%",
            "cpp": "70%",
            "c#": "120%"
    },
    "Abouelhassan": {
        "c": "80%",
        "cpp": "20%",
        "c#": "80%"
    }
}
for name in people:
    print(f"skills and progress for {name} is: {people[name]}")
    for skill in people[name]:
        print(f"{skill}=>{people[name]}")