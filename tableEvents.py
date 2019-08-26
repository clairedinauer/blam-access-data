import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import predCode_participant_list  # predictive coding participant list
import predCode_table_of_events  # predictive coding table of events list

# Link to the practice_accesscheck.xlsx Excel sheet
# This sheet covers the "Access" data entry checklist

print("This system will pull up a participant's Table of Events.\n")
df = pd.read_excel(r'practice_accesscheck.xlsx', sheet_name='TABLE OF EVENTS')

beliefid = str.upper((input('Please enter BeliefID: ')))


if beliefid in predCode_participant_list.belieflist:
    print("\nBeliefID found. Here is what I have on file for " + beliefid + ":")

    # this selects all rows where the participant id is equal to the user input
    df_temp = df[df['MPRCID'] == beliefid]

    # this resets the index to regular, so we can just use iloc(0)
    df_temp = df_temp.reset_index()

    for i in predCode_table_of_events.toeForms:
        if df_temp.loc[0, i] == 'no':
            print(i + ' missing')

    print('NOTES:')
    print(df.loc[df.MPRCID == beliefid, 'NOTES'])

else:
    print("Sorry, I do not have " + beliefid + " on file.")
