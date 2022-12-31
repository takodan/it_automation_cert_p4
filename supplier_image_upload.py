#!/usr/bin/env python3

# supplier_image_upload

import requests
import os
import re

def get_files_in_dir(dir_path):
    """return target files in a list"""
    items_list = os.listdir(dir_path)
    item =""
    files_list = []
    for item in items_list:
        # check isfile jpeg
        if os.path.isfile(os.path.join(dir_path, item)):
            if re.search(r"\.jpeg", os.path.join(dir_path, item)) != None:
                files_list.append(item)

    print(files_list)
    return files_list

def main():
    source_dir = os.path.abspath(input("please enter the source directory: "))
    print(source_dir)
    images_list = get_files_in_dir(source_dir)

    url = input("please enter the url: ")
    print(url)
    response = requests.get(url)
    print(response.ok)
    # if response.ok:
    for image in images_list:
            print(os.path.join(source_dir, image))
            with open(os.path.join(source_dir, image), "rb") as opend:
                response = requests.post(url, files={"file": opend})
                print(source_dir + "_"+ str(response.ok))

if __name__ == "__main__":
    main()
