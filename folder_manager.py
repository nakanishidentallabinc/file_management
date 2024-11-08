
'''
<summary>
This module contains functions for managing folders and their contents.
</summary>
<copyright file="folder_manager.py" company="Nakanishi Dental Lab, Inc.">
Copyright (c) Nakanishi Dental Lab, Inc. All rights reserved. 11/8/2024
</copyright>
'''

import os
import shutil
import logging

class FolderManager:
    def copy_contents(self, target_directory, folder_map):
        os.makedirs(target_directory, exist_ok=True)
        for folder_name, source_folder_path in folder_map.items():
            target_folder_path = os.path.join(target_directory, folder_name)
            os.makedirs(target_folder_path, exist_ok=True)
            logging.info(f"Created: {target_folder_path}")
            self._copy_folder_contents(source_folder_path, target_folder_path)

    def list_all_folders(self, source_directory):
        all_folders = [folder for folder in os.listdir(source_directory) 
                       if os.path.isdir(os.path.join(source_directory, folder))]
        if all_folders:
            print("All folders found:")
            for folder in all_folders:
                print(folder)
        else:
            print("No folders found in the specified directory.")

    def list_zip_files(self, source_directory):
        zip_files = [file for file in os.listdir(source_directory) 
                     if file.lower().endswith('.zip')]
        if zip_files:
            print("Found ZIP files:")
            for zip_file in zip_files:
                print(zip_file)
        else:
            print("No ZIP files found in the specified directory.")
        return zip_files

    def display_found_folders(self, found_folders):
        logging.info("Found folders/files:")
        for name, path in found_folders.items():
            logging.info(f"{name}: {path}")

    def _copy_folder_contents(self, source_folder_path, target_folder_path):
        try:
            for item_name in os.listdir(source_folder_path):
                source_item_path = os.path.join(source_folder_path, item_name)
                target_item_path = os.path.join(target_folder_path, item_name)
                if os.path.isdir(source_item_path):
                    shutil.copytree(source_item_path, target_item_path)
                    logging.info(f"Copied directory: {source_item_path} to {target_item_path}")
                else:
                    shutil.copy2(source_item_path, target_item_path)
                    logging.info(f"Copied file: {source_item_path} to {target_item_path}")
        except Exception as e:
            logging.error(f"Error copying contents from {source_folder_path} to {target_folder_path}: {e}")