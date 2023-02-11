import os
import plistlib

def delete_safari_history():
    # The location of the Safari history file
    history_file = "/Users/UserName/Library/Safari/History.plist"

    # Check if the history file exists
    if os.path.exists(history_file):
        # Remove the history file
        os.remove(history_file)

        # Print a message indicating that the history has been deleted
        print("Safari history deleted.")
    else:
        # Print a message indicating that the history file was not found
        print("Safari history not found.")
