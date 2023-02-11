import os
import shutil

def delete_chrome_history():
    # The location of the Google Chrome history file
    history_file = "C:\\Users\\UserName\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

    # Check if the history file exists
    if os.path.exists(history_file):
        # Remove the history file
        os.remove(history_file)

        # Remove the history-journal directory
        shutil.rmtree("C:\\Users\\UserName\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History-Journal")

        # Print a message indicating that the history has been deleted
        print("Google Chrome history deleted.")
    else:
        # Print a message indicating that the history file was not found
        print("Google Chrome history not found.")
