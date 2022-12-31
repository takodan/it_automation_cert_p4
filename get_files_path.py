#!/usr/bin/env python3

# get_files_path
import os
import re

def get_files_in_dir(dir_path):
    """return target files in a list"""
    items_list = os.listdir(dir_path)
    item =""
    files_list = []
    for item in items_list:
        # check isfile tiff
        if os.path.isfile(os.path.join(dir_path, item)):
            if re.search(r"\.txt", os.path.join(dir_path, item)) != None:
                files_list.append(item)

    # check print(files_list)
    return files_list

def main():
    pass


if __name__ == "__main__":
    main()
