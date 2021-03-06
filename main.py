__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import os.path
import zipfile


def clean_cache():
    path = os.getcwd()
    path_cache = os.path.join(path, "cache")
    if os.path.exists(path_cache) == True:
        for f in os.listdir(path_cache):
            os.remove(os.path.join(path_cache, f))
    else:
        os.mkdir("cache")


def cache_zip(zip_file_path, cache_dir_path):
    z_file = zipfile.ZipFile(zip_file_path)
    z_file.extractall(cache_dir_path)


def cached_files():
    all_files = []
    path = os.getcwd()
    path_cache = os.path.join(path, "cache")
    for f in os.listdir(path_cache):
        all_files.append(path_cache + "/" + f)
    return all_files


def find_password(all_files):
    for file in all_files:
        with open(file, 'r') as f:
            text = f.readlines()
            for line in text:
                if 'password' in line:
                    password = line.split(" ")
                    return str(password[1]).strip()
