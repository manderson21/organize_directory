import os
import argparse

parser = argparse.ArgumentParser(description="Cleanup directory and put files into desired folders")

parser.add_argument("--path", type=str, default=".", help="Directory path to clean up")

args = parser.parse_args()
path = args.path

# Get all the files of the path
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

for doc in docs:
    full_doc_path, doc_ext = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    if doc_name == "main":
        continue

    # Create subfolder
    subfolder_path = os.path.join(path, doc_ext[1:].lower())

    if subfolder_path not in folders:
        try:
            os.mkdir(subfolder_path)
            print(f"Folder {subfolder_path} created.")
        except FileExistsError as e:
            print(f"Could not create folder at {subfolder_path}... {e}")

    # Move document
    new_doc_path = os.path.join(subfolder_path, doc_name) + doc_ext
    os.rename(doc, new_doc_path)

