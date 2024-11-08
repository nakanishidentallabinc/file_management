
'''
<summary>
This module contains functions for extracting ZIP files.
</summary>
<copyright file="extract_zip.py" company="Nakanishi Dental Lab, Inc.">
Copyright (c) Nakanishi Dental Lab, Inc. All rights reserved. 11/8/2024
</copyright>
'''

import os
import zipfile
import logging

class ZipExtractor:
    def extract_zip_file(self, zip_file_path, dest_folder):
        os.makedirs(dest_folder, exist_ok=True)
        folder_name = os.path.splitext(os.path.basename(zip_file_path))[0]
        extract_path = os.path.join(dest_folder, folder_name)

        try:
            os.makedirs(extract_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            logging.info(f"Extracted: {zip_file_path} to {extract_path}")
        except zipfile.BadZipFile:
            logging.error(f"Bad ZIP file: {zip_file_path}")
        except Exception as e:
            logging.error(f"Failed to extract {zip_file_path}: {e}")