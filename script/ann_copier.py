import os
import shutil

def copy_and_rename(source_dir, destination_dir, old_prefix, new_prefix):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    # Check if the destination directory exists, if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # List all files in the source directory
    files = os.listdir(source_dir)
    
    for file in files:
        # Check if the item is a file (not a directory)
        if os.path.isfile(os.path.join(source_dir, file)):
            # Check if the file name starts with the old prefix
            if file.startswith(old_prefix):
                # Construct the new file name
                new_file_name = file.replace(old_prefix, new_prefix)
                # Construct the new file path in the destination directory
                new_file_path = os.path.join(destination_dir, new_file_name)
                # Copy and rename the file to the destination directory
                shutil.copyfile(os.path.join(source_dir, file), new_file_path)
                print(f"File '{file}' copied and renamed to '{new_file_path}'")