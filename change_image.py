#!/usr/bin/env python3

# change_image
import os
import re
from PIL import Image

def get_files_in_dir(dir_path):
    """return target files in a list"""
    items_list = os.listdir(dir_path)
    item =""
    files_list = []
    for item in items_list:
        # check isfile tiff
        if os.path.isfile(os.path.join(dir_path, item)):
            if re.search(r"\.tiff", os.path.join(dir_path, item)) != None:
                files_list.append(item)

    print(files_list)
    return files_list


def resize_convert_image(im_class, dest_path):
    print(dest_path[:-4]+"jpeg")
    im_resized = im_class.resize((600, 400))
    im_resized.convert('RGB').save( dest_path[:-4]+"jpeg", "JPEG" ) # file name might change

def main():
    source_dir = ""
    dest_dir = ""
    while True:
        source_dir = input("please enter the source directory abspath: ")
        dest_dir = input("please enter the destination directory abspath: ")
        # valid path
        print(source_dir, dest_dir)
        if os.path.isdir(source_dir) and os.path.isdir(dest_dir) :
            print("directory valid")
            break
        else:
            print("directory invalid")

    images_list = get_files_in_dir(source_dir)

    for image in images_list:
        dest_path = os.path.join(dest_dir, image)
        with Image.open(os.path.join(source_dir, image)) as im_class:
            resize_convert_image(im_class, os.path.join(source_dir, image))


if __name__ == "__main__":
    main()