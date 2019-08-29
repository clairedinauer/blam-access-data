import pandas as pd
import predCode_participant_list  # predictive coding participant list
import predCode_table_of_events  # predictive coding table of events list
from time import sleep as s

# Link to the practice_accesscheck.xlsx Excel sheet
# This sheet covers the "Access" data entry checklist

print("This system will pull up a participant's Table of Events.\n")
s(1)

df = pd.read_excel(r'practice_accesscheck.xlsx', sheet_name='TABLE OF EVENTS')

for beliefid in predCode_participant_list.belieflist:
    print("\nParticipant " + beliefid + " is missing:")

    # this selects all rows where the participant id is equal to the user input
    df_temp = df[df['MPRCID'] == beliefid]

    # this resets the index to regular, so we can just use iloc(0)
    df_temp = df_temp.reset_index()

    for i in predCode_table_of_events.toeForms:
        if df_temp.loc[0, i] == 'no':
            print(i)

    print('NOTES:')
    print(df.loc[df.MPRCID == beliefid, 'NOTES'])
