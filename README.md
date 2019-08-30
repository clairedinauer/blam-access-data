# blam-access-data
    excelData Folder:
        -- Includes the record of participants' completion of Table of Events
        -- Includes "practice_accesscheck.xlsx" which has the record of both "ACCESS" and "TABLE OF EVENTS" completion

    oldToeAccessFunctions Folder:
      -- Includes the previous Python files used to either lookup a participant's completion of Table of Events or Access Data entry ('accesscheck.py' and 'tableEvents.py'), or list all participants' completion ('accesscheck_ALL.py' and 'tableEvents_ALL.py')

    predCode Folder:
      -- Includes the code focused on carrying out the previously listed tasks. The user may choose which task they would like to carry out. This is in "predictive_coding_tracking.py".
      -- Includes "lists" folder, which holds the list of participants, access forms, and table of events forms. This folder also has the .txt file lists for appending participants. practice_checklist.xlsx

# Notes to Self for Future Improvements:

    -- The next thing I would like to tackle, specifically in predictive_coding_tracking_classes.py, is to create a loop for the add() and remove() functions if the user wishes to add or remove multiple Belief IDs.
    -- I would also like to create a loop for the numbered menu that users will return to after completing their desired function. In other words, the program will re-run the menu after each task until the user enters "5" to exit.
