'''
<summary>
This module contains functions for finding missing case numbers in a specified directory.
</summary>
<copyright file="checking_missing_cases.py" company="Nakanishi Dental Lab, Inc.">
Copyright (c) Nakanishi Dental Lab, Inc. All rights reserved. 11/8/2024
</copyright>
'''
import os

# Modified CaseChecker class
class CaseChecker:
    def find_missing_cases(self, directory_path, case_numbers):
        folder_map = self._get_folder_map(directory_path)
        results = self._search_folders(folder_map, case_numbers)
        found_case_numbers = self._extract_case_numbers(results)
        missing_cases = set(case_numbers) - set(found_case_numbers)
        return missing_cases, found_case_numbers

    def _get_folder_map(self, directory_path):
        return {folder_name: os.path.join(directory_path, folder_name)
                for folder_name in os.listdir(directory_path)
                if os.path.isdir(os.path.join(directory_path, folder_name))}

    def _search_folders(self, folder_map, case_numbers):
        return {folder_name: folder_path
                for folder_name, folder_path in folder_map.items()
                if any(case_number in folder_name for case_number in case_numbers)}

    def _extract_case_numbers(self, results):
        found_case_numbers = []
        for folder in results.keys():
            parts = folder.split('-')
            if len(parts) > 1:
                found_case_numbers.append(parts[1])
        return found_case_numbers