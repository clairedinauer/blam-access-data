import pandas as pd
import predCode_participant_list  # predictive coding participant list
import predCode_table_of_events  # predictive coding table of events list
import predCode_access_db
from time import sleep as s

# Link to the practice_accesscheck.xlsx Excel sheet
# This sheet covers the "Access" data entry checklist

temp = []

df = pd.read_excel(r'practice_accesscheck.xlsx', sheet_name='TABLE OF EVENTS')


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


def lookup():
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
        df = pd.read_excel(r'practice_accesscheck.xlsx', sheet_name='ACCESS')
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


def listall():
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
        df = pd.read_excel(r'practice_accesscheck.xlsx', sheet_name='ACCESS')

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


def add():
    beliefid = str.upper((input('Please enter BeliefID: ')))
    # if beliefid not in predCode_participant_list.belieflist:
    #     predCode_participant_list.belieflist.append(beliefid)
    #     print("Updated List: " + predCode_participant_list.belieflist)
    # elif beliefid in predCode_participant_list.belieflist:
    #     print("This BeliefID already exists.")

    # if beliefid not in predCode_participant_list.belieflist:
    #     predCode_participant_list.belieflist.append(beliefid)
    # else:
    #     print("This BeliefID already exists.")
    with open('list.txt', 'a') as filehandle:
        # if beliefid not in filehandle:
        # needs to traverse the whole file
        filehandle.writelines("'" + beliefid + "'',\n")
        # else:
        #     print("This BeliefID already exists.")


if __name__ == "__main__":
    select()
    if selection == 1:
        lookup()
        lookupAccess()
    elif selection == 2:
        listall()
        listallAccess()
    elif selection == 3:
        add()
    elif selection == 4:
        remove()
    elif selection == 5:
        print("Until next time, my friend :)")
        s(2)
        exit()
