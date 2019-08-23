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

beliefid = ['M042300',
'M042311',
'M042322',
'M042333',
'M042344',
'M042355',
'M042366',
'M042377',
'M042388',
'M042390',
'M042401',
'M042412',
'M042423',
'M042434',
'M042445',
'M042456',
'M042467',
'M042478',
'M042480',
'M042491',
'M042502',
'M042513',
'M042524',
'M042535',
'M042546',
'M042557',
'M042568',
'M042570',
'M042581',
'M042592',
'M042603',
'M042614',
'M042625',
'M042636',
'M042647',
'M042658',
'M042660',
'M042671',
'M042682',
'M042693',
'M042704',
'M042715',
'M042726',
'M042737',
'M042748',
'M042750',
'M042761',
'M042772',
'M042783',
'M042794'
]
