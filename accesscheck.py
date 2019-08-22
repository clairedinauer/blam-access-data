import pandas as pd
import numpy as np

#Link to the practice_accesscheck.xlsx Excel sheet
#This sheet covers the "Access" data entry checklist

print("This system will indicate if a participant's forms have been entered in Access.\n")
df = pd.read_excel('practice_accesscheck.xlsx')

beliefid = str.upper((input('Please enter BeliefID: ')))
belieflist = [
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
'M042570'
]

if beliefid in belieflist:
    print ("\nBeliefID found. Here is what I have on file for " + beliefid + ":")

    #this selects all rows where the participant id is equal to the user input
    df_temp = df[df['MPRCID'] == beliefid]

    #this resets the index to regular, so we can just use iloc(0)
    df_temp = df_temp.reset_index()

    #
    forms = [
    'Medical History',
    'ConCom Meds',
    'NonPychCC Meds',
    'NUQ',
    'DDF5',
    'SCID5 Summary',
    'MATRICS',
    'Hollow Mask Illusion',
    'BPRS',
    'CHAT',
    'CAINS',
    'LOF',
    'WAMHI'
    ]

    for i in forms:
        if df_temp.loc[0, i] == 'no':
            print(i + ' missing')

else:
    print("Sorry, I do not have " + beliefid + " on file.")
