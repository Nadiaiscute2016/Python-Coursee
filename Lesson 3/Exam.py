medical_cause=input("Did you have a medical cause? Yes or  No: ")
attend=int(input("Enter the attendance of a student."))
if medical_cause=='Yes':
    print("You are allowed.")
else:
    if attend>=75:
     print("Allowed")
    else:
     print(" Not Allowed")