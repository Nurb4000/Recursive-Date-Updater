import easygui
import os
import time

def modify_modification_time(path, timestamp):
    # Change the modification and access times of the file or folder
    os.utime(path, (timestamp, timestamp))

def traverse_and_modify(folder):
    # Traverse all subfolders and files in alphabetical order
    for root, dirs, files in os.walk(folder, topdown=True):
        # Sort directories and files in alphabetical order
        dirs.sort()
        files.sort()

        # Modify the modification date/time of each directory
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            print(f'Modifying directory: {dir_path}')
            modify_modification_time(dir_path, time.time())

        # Modify the modification date/time of each file
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f'Modifying file: {file_path}')
            modify_modification_time(file_path, time.time())

# Main program
if __name__ == "__main__":
    folder = easygui.diropenbox(msg="Select a folder", title="Folder Selection", default='.')
    
    if folder:
        print(f'Selected folder: {folder}')
        traverse_and_modify(folder)
    else:
        print('No folder selected.')
