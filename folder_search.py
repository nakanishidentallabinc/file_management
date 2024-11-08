
'''
<summary>
This module contains functions for searching folders based on various criteria.
</summary>
<copyright file="folder_search.py" company="Nakanishi Dental Lab, Inc.">
Copyright (c) Nakanishi Dental Lab, Inc. All rights reserved. 11/8/2024
</copyright>
'''


import os

class FolderSearcher:
    def search_by_case_numbers(self, source_directory, case_numbers):
        folder_map = self._get_folder_map(source_directory)
        return {name: path for name, path in folder_map.items() 
                if any(case_number in name for case_number in case_numbers)}

    def search_by_name(self, source_directory, search_terms):
        folder_map = self._get_folder_map(source_directory)
        return {name: path for name, path in folder_map.items() 
                if any(term.lower() in name.lower() for term in search_terms)}

    def pan_search(self, source_directory, query):
        folder_map = self._get_folder_map(source_directory)
        return {name: path for name, path in folder_map.items() 
                if query.lower() in name.lower()}

    def _get_folder_map(self, source_directory):
        return {folder_name: os.path.join(source_directory, folder_name)
                for folder_name in os.listdir(source_directory)
                if os.path.isdir(os.path.join(source_directory, folder_name))}