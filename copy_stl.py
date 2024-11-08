
'''
<summary>
This module contains functions for copying and renaming STL files.
</summary>
<copyright file="copy_stl.py" company="Nakanishi Dental Lab, Inc.">
Copyright (c) Nakanishi Dental Lab, Inc. All rights reserved. 11/8/2024
</copyright>
'''

import os
import shutil

class STLFileHandler:
    def copy_stl_files(self, source_folders, target_directory, rename=False):
        """Copies STL files from source folders to the target directory."""
        os.makedirs(target_directory, exist_ok=True)
        
        for folder_path in source_folders:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.lower().endswith('.stl'):
                        source_file = os.path.join(root, file)
                        if rename:
                            new_name = f"{os.path.splitext(file)[0]}_copy.stl"
                        else:
                            new_name = file
                        target_file = os.path.join(target_directory, new_name)
                        try:
                            shutil.copy2(source_file, target_file)
                            print(f"Copied: {source_file} -> {target_file}")
                        except Exception as e:
                            print(f"Error copying {source_file}: {str(e)}")

    def rename_stl_files_with_structure(self, source_folders, target_directory):
        """Copies and renames .stl files and their containing folders."""
        for source_folder in source_folders:
            relative_path = os.path.relpath(source_folder, os.path.dirname(source_folder))
            new_folder_name = f"{relative_path}_copy"
            new_folder_path = os.path.join(target_directory, new_folder_name)

            try:
                os.makedirs(new_folder_path, exist_ok=True)
                print(f"Created folder: {new_folder_path}")
            except Exception as e:
                print(f"Error creating folder {new_folder_path}: {e}")
                continue

            for root, _, files in os.walk(source_folder):
                for file in files:
                    if file.lower().endswith('.stl'):
                        old_path = os.path.join(root, file)
                        relative_file_path = os.path.relpath(old_path, source_folder)
                        new_name = f"{os.path.splitext(relative_file_path)[0]}_copy.stl"
                        new_path = os.path.join(new_folder_path, new_name)
                        try:
                            os.makedirs(os.path.dirname(new_path), exist_ok=True)
                            shutil.copy2(old_path, new_path)
                            print(f"Copied and renamed: {old_path} -> {new_path}")
                        except Exception as e:
                            print(f"Error copying and renaming {old_path}: {e}")