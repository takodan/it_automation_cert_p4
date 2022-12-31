#! /usr/bin/env python3

# process txt to json, save json to cwd, and post json to url

import os
import requests
import json
from get_files_path import get_files_in_dir

def process_txt_files(file_path, name):
    output_dict = {}
    with open(file_path, "r") as f:
        output_dict["name"] = f.readline().strip()
        output_dict["weight"] = int(f.readline().strip(" lbs\n"))
        output_dict["description"] = f.readline().strip()
        output_dict["image_name"] = name[:-3]+"jpeg"

    return output_dict


def main():
    source_dir = os.path.abspath(input("please enter the source directory: "))
    files_list = get_files_in_dir(source_dir)
    print(files_list)

    fruits_list = []
    for f in files_list:
        dict = process_txt_files(os.path.join(source_dir, f), f)
        print(dict)
        fruits_list.append(dict)

    # check print(fruits_list)

    json_file_path = os.path.join(os.getcwd(), "fruits.json")
    with open(json_file_path, "w") as f_json:
        json.dump(fruits_list, f_json)

    url = input("please enter the url: ")
    response = requests.get(url)
    if response.ok:
        for fruit in fruits_list:
            response = requests.post(url, json=fruit)
            print(response.ok)

if __name__ == "__main__":
    main()
