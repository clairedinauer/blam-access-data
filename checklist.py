BeliefID = str(input("Please enter BeliefID: "))
belieflist = ["000001", "000002", "000003", "000004", "000005"]

if BeliefID in belieflist:
    print ("Great, let me pull up data for participant " + BeliefID +".")

    if BeliefID == "000001" or "000002" or "000003" or "000004" or "000005":
        checklist = str(input("Which form do you want to confirm? "))
        if checklist == "Medical History" and BeliefID == "000001":
            print("This form is completed.")
        else:
            print("This form is missing.")

else:
    print("Sorry, I do not have " + BeliefID + " on file.")
