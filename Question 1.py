#Emily Nixon Sarah Stephenson
stud_dict={
    "Sarah" : "90",
    "Emily" : "85",
    "Jonathan" : "48",
    "Madison" : "29" ,
    "George" : "51"
}
def stud_grades(stud_dict):
    for name in stud_dict:
        if stud_dict[name] < "50":
            print(name)
        else:
            None

stud_grades(stud_dict)

