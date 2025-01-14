import os
import shutil
import random

def split_data(image_folder, label_folder, output_folder):
    """
    Split images and labels into train, validation, and test sets.

    Parameters:
        image_folder (str): Path to the folder containing images.
        label_folder (str): Path to the folder containing labels.
        output_folder (str): Path to the output folder where data will be organized.
    """
    # Create the necessary folder structure
    subsets = ['train', 'val', 'test']
    for subset in subsets:
        os.makedirs(os.path.join(output_folder, 'images', subset), exist_ok=True)
        os.makedirs(os.path.join(output_folder, 'labels', subset), exist_ok=True)

    # Get all image and label files
    image_files = sorted([f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))])
    label_files = sorted([f for f in os.listdir(label_folder) if os.path.isfile(os.path.join(label_folder, f))])

    # Ensure there is a corresponding label for each image
    paired_files = [(img, lbl) for img, lbl in zip(image_files, label_files) if os.path.splitext(img)[0] == os.path.splitext(lbl)[0]]

    if len(paired_files) < 270:
        raise ValueError("Not enough image-label pairs to satisfy the requested split.")

    # Shuffle the files for random distribution
    random.shuffle(paired_files)

    # Split the data
    train_files = paired_files[:200]
    val_files = paired_files[200:250]
    test_files = paired_files[250:]

    # Function to copy files to the appropriate directories
    def copy_files(file_list, subset):
        for img_file, lbl_file in file_list:
            shutil.copy(os.path.join(image_folder, img_file), os.path.join(output_folder, 'images', subset, img_file))
            shutil.copy(os.path.join(label_folder, lbl_file), os.path.join(output_folder, 'labels', subset, lbl_file))

    # Copy files to train, val, and test directories
    copy_files(train_files, 'train')
    copy_files(val_files, 'val')
    copy_files(test_files, 'test')

    print("Data split and copied successfully!")

# Example usage
image_dir = r"c:\Users\Nishita Gopi\Documents\image_named"
label_dir = r"c:\Users\Nishita Gopi\Documents\labels"
output_dir = r"C:\Users\Nishita Gopi\Documents\sampling"
split_data(image_dir, label_dir, output_dir)
