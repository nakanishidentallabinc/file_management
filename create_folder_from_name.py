import os
import shutil

def create_folders_and_move_files(base_directory):
    # Change to the specified base directory
    os.chdir(base_directory)

    # List all files in the directory
    files = os.listdir(base_directory)

    # Dictionary to hold folder names and their corresponding files
    folder_dict = {}

    for file in files:
        # Check if the file ends with .stl or is an Antag file
        if file.endswith('.stl'):
            # Extract the folder name from the .stl file
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif 'Antag' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif '0' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif '1' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif '2' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif '3' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif '4' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif 'UnsectionedModel_LowerJaw' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif 'UnsectionedModel_UpperJaw' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        elif 'Tooth' in file:
            # Extract the folder name from Antag files
            folder_name = file.split('_')[0]  # Get the part before the first underscore
            folder_dict.setdefault(folder_name, []).append(file)
        

    # Create folders and move files into them
    for folder_name, files in folder_dict.items():
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Move each file into the corresponding folder
        for file in files:
            shutil.move(file, os.path.join(folder_name, file))

    print("Folders created and files moved successfully.")

# Specify your base directory here
base_directory = r'C:\Users\design2\Downloads'  # Change this to your target directory

create_folders_and_move_files(base_directory)