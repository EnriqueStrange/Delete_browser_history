import os
import sqlite3

def delete_firefox_history():
    # The location of the Mozilla Firefox history file
    history_file = "C:\\Users\\UserName\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*.default\\places.sqlite"

    # Check if the history file exists
    if os.path.exists(history_file):
        # Connect to the history database
        conn = sqlite3.connect(history_file)
        c = conn.cursor()

        # Delete the data from the 'moz_places' and 'moz_historyvisits' tables
        c.execute("DELETE FROM moz_places;")
        c.execute("DELETE FROM moz_historyvisits;")

        # Commit the changes to the database and close the connection
        conn.commit()
        conn.close()

        # Print a message indicating that the history has been deleted
        print("Firefox history deleted.")
    else:
        # Print a message indicating that the history file was not found
        print("Firefox history not found.")
