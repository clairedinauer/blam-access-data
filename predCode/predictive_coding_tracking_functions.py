'''
This script allows the user to select, view, add, and remove subjects from the Predictive Coding study's participant tracking database.

The layout is in functions.
'''

import pandas as pd
import predCode_participant_list  # import participant list (subject IDs)
import predCode_table_of_events  # import table of events list
import predCode_access_db  # import access database list
from time import sleep as s  # allows for pauses in display time

# Link to the predCode_table_of_events.xlsx Excel sheet
# This sheet covers the "Table of Events" data entry checklist
df = pd.read_excel(r'excelData/predCode_table_of_events.xlsx', sheet_name='TABLE OF EVENTS')


def select():
    print("Welcome to Predictive Coding Study Particpant Tracking Database.\n")
    s(1)
    print("1. Lookup specific participant ID.")
    print("2. List all missing data from all subjects.")
    print("3. Add new subject to database.")
    print("4. Remove subject from database.")
    print("5. Bye!\n")
    global selection
    selection = int(input("What would you like to do? "))
    s(1)


def lookupTOE():
    global beliefid
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


def lookupAccess():
    s(1)
    access = str(input("\nWould you also like to see what is missing for " +
                       beliefid + " in Access? (y/n) "))
    if access == 'y':
        df = pd.read_excel(r'excelData/predCode_table_of_events.xlsx', sheet_name='ACCESS')
        if beliefid in predCode_participant_list.belieflist:
            print("\n" + beliefid + " is missing the following forms in Access:")

            # this selects all rows where the participant id is equal to the user input
            df_temp = df[df['MPRCID'] == beliefid]

            # this resets the index to regular, so we can just use iloc(0)
            df_temp = df_temp.reset_index()

            for i in predCode_access_db.forms:
                if df_temp.loc[0, i] == 'no':
                    print(i + ' missing')
        else:
            print("Sorry, I do not have " + beliefid + " on file.")

    else:
        exit()


def listallTOE():
    for beliefid in predCode_participant_list.belieflist:
        print("\nParticipant " + beliefid + " is missing:")

        # this selects all rows where the participant id is equal to the user input
        df_temp = df[df['MPRCID'] == beliefid]

        # this resets the index to regular, so we can just use iloc(0)
        df_temp = df_temp.reset_index()

        for i in predCode_table_of_events.toeForms:
            if df_temp.loc[0, i] == 'no':
                print('   ' + i)

        print('NOTES:')
        print(df.loc[df.MPRCID == beliefid, 'NOTES'])


def listallAccess():
    s(1)
    access = str(input("\nWould you like to list who is missing which forms in Access? (y/n) "))
    if access == 'y':
        df = pd.read_excel(r'excelData/predCode_table_of_events.xlsx', sheet_name='ACCESS')

        for beliefid in predCode_participant_list.belieflist:
            print("\nParticipant " + beliefid + " is missing:")

            # this selects all rows where the participant id is equal to the user input
            df_temp = df[df['MPRCID'] == beliefid]

            # this resets the index to regular, so we can just use iloc(0)
            df_temp = df_temp.reset_index()

            for i in predCode_access_db.forms:
                if df_temp.loc[0, i] == 'no':
                    print(i)
        else:
            exit()


def add():  # allows the uer to add a new BeliefID
    beliefid = str.upper((input('Please enter new BeliefID: ')))

    # This checks if the BeliefID is already in the list:
    with open('list.txt') as f:
        if beliefid in f.read():
            print("This BeliefID is already taken.")
            return  # Insert "return" to avoid adding a beliefid that already exists

    # This adds the new beliefid to the text file using append through 'a' and 'writelines':
    with open('list.txt', 'a') as filehandle:
        filehandle.writelines("'" + beliefid + "',\n")
        print("BeliefID successfully added. Remember to save the 'list.txt' file.")
        return


def remove():
    beliefid = str.upper((input('Please enter BeliefID: '))).strip()

    # This checks if the BeliefID is not in the list:
    with open('list.txt') as f:
        if beliefid not in f.read():
            print("This BeliefID is not in the list, and therefore cannot be removed.")
            return

    # If the BeliefID is in the list, it will be deleted:
    with open('list.txt', 'r+') as f:
        t = f.read()
        beliefid_delete = beliefid.strip()
        f.seek(0)
        for line in t.split('\n'):
            if line != beliefid_delete:
                f.write(line + '\n')
        f.truncate()
        print("BeliefID successfully deleted. Remember to save the 'list.txt' file.")


if __name__ == "__main__":
    select()
    if selection == 1:
        lookupTOE()
        lookupAccess()
    elif selection == 2:
        listallTOE()
        listallAccess()
    elif selection == 3:
        add()
    elif selection == 4:
        remove()
    elif selection == 5:
        print("Until next time, my friend :)")
        s(2)
        exit()
