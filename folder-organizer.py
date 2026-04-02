import os
import argparse
from time import sleep
import sys

target_folders = ["PDFs", "Images", "Documents", "Archives", "Folders", "Other"]

def create_folders(target_folders, chosen_path):

    for folder in target_folders:
        folder_path = os.path.join(chosen_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_folder(target_folders, chosen_path, verbose_mode=False):

    files_and_folders = os.listdir(chosen_path)
    animation_output = ["|", "/", "-", "\\"]
    animation_step = 0

    for file in files_and_folders:

        file_path = os.path.join(chosen_path, file)

        if file in target_folders:
            continue  # Skip the folders we created
        elif file.endswith(".pdf"):
            os.rename(file_path, os.path.join(chosen_path, "PDFs", file))
        elif file.endswith(".jpg") or file.endswith(".png"):
            os.rename(file_path, os.path.join(chosen_path, "Images", file))
        elif file.endswith(".docx") or file.endswith(".txt"):
            os.rename(file_path, os.path.join(chosen_path, "Documents", file))
        elif file.endswith(".zip") or file.endswith(".rar"):
            os.rename(file_path, os.path.join(chosen_path, "Archives", file))
        elif os.path.isdir(file_path):
            os.rename(file_path, os.path.join(chosen_path, "Folders", file))
        else:
            os.rename(file_path, os.path.join(chosen_path, "Other", file))

        if verbose_mode:
            print(f"Organized: {file}")
            sleep(0.1)  # Simulate some delay for better visualization
        else:
            print(f"Operation ongoing      {animation_output[animation_step % len(animation_output)]}", end="\r")
            animation_step += 1
            sleep(0.05)  # Simulate some delay for better visualization
    
    print(f"\nOrganization complete! Files and folders organized: {len(files_and_folders)}")
            
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Folder Organizer")

    parser.add_argument("--path", 
                        type=str, 
                        default=os.path.expanduser("~/Downloads"), 
                        help="Path to folder which needs to be organized (default: ~/Downloads)"
                        )

    parser.add_argument("--verbose", 
                        action="store_true",
                        help="Print organized files"
                        )

    args = parser.parse_args()
    chosen_path = args.path
    verbose_mode = args.verbose

    if not os.path.exists(chosen_path):
        print(f"\nERROR: The path '{chosen_path}' does not exist.\n")
        sys.exit(1)

    create_folders(target_folders, chosen_path)
    organize_folder(target_folders, chosen_path, verbose_mode)