import pandas as pd
import predCode  # predictive coding participant list
import predCode_access_db  # predictive coding access checklist

# Link to the practice_accesscheck.xlsx Excel sheet
# This sheet covers the "Access" data entry checklist

print("This system will indicate if a participant's forms have been entered in Access.\n")
df = pd.read_excel(r'practice_accesscheck.xlsx', sheet_name='ACCESS')

beliefid = str.upper((input('Please enter BeliefID: ')))

if beliefid in predCode.belieflist:
    print("\nBeliefID found. Here is what I have on file for " + beliefid + ":")

    # this selects all rows where the participant id is equal to the user input
    df_temp = df[df['MPRCID'] == beliefid]

    # this resets the index to regular, so we can just use iloc(0)
    df_temp = df_temp.reset_index()

    for i in predCode_access_db.forms:
        if df_temp.loc[0, i] == 'no':
            print(i + ' missing')

else:
    print("Sorry, I do not have " + beliefid + " on file.")
