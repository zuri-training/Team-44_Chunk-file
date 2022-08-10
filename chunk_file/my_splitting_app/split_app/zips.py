import os
from zipfile import ZipFile
from flask import send_file


def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def zipper(filename, username):
    # path to folder which needs to be zipped

    directory = "./static/uploads"

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # writing files to a zipfile
    with ZipFile(
        f"C:/Users/Abdolyom/Desktop/FINAL PROJECT\Team-44_Chunk-file\chunk_file\my_splitting_app/split_app/static/uploads/{username}_{filename}.zip",
        "w",
    ) as zip:
        # writing each file one by one
        for file in file_paths:
            newfile = file.split(".")
            if len(newfile) > 1:
                if newfile[-1] == "csv" or newfile[-1] == "json":
                    zip.write(file)
                    os.remove(file)
