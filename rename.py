import os
import shutil

def rename_files(src_dir, dest_dir):
    """
    Rename all files from src_dir and save them to dest_dir with sequential names.

    Parameters:
        src_dir (str): The source directory containing the original files.
        dest_dir (str): The destination directory to save the renamed files.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Enumerate through the files in the source directory
    for index, file_name in enumerate(os.listdir(src_dir), start=1):
        file_path = os.path.join(src_dir, file_name)
        
        # Skip directories, process files only
        if not os.path.isfile(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(file_name)

        # Define the new file name
        new_file_name = f"image{index}{file_extension}"
        new_file_path = os.path.join(dest_dir, new_file_name)

        # Copy and rename the file to the destination directory
        shutil.copy(file_path, new_file_path)
        print(f"Renamed and copied: {file_name} -> {new_file_name}")

# Usage example
source_directory = r"C:\Users\Nishita Gopi\Documents\image"
destination_directory = r"C:\Users\Nishita Gopi\Documents\image_named"
rename_files(source_directory, destination_directory)
