import os
import shutil

rootDir = 'C:/'
destination = "C:/Users/James.Hannafin/Desktop/Gate Fees"

if not os.path.exists(destination):
    os.makedirs(destination)

for dirName, subdirList, fileList in os.walk(rootDir):
    for filename in fileList:
        if filename.startswith("GateFees"):
            src_file = os.path.join(dirName, filename)
            dst_file = os.path.join(destination, filename)
            shutil.move(src_file, dst_fiimport os
import shutil

# Define the source directory (where your files are located)
source_directory = os.path.expanduser("~/Desktop")

# Define the destination directories for different prefixes
destination_directories = {
    "dream": os.path.expanduser("~/Documents/Dream"),
    "cyberfield": os.path.expanduser("~/Documents/Cyberfield"),
    "gatefees": os.path.expanduser("~/Documents/Gate Fees"),
}

# Create the destination folders if they don't exist
for destination in destination_directories.values():
    os.makedirs(destination, exist_ok=True)

# Function to move files based on their prefix
def move_file(filename, source_directory):
    source_filepath = os.path.join(source_directory, filename)
    for prefix, destination in destination_directories.items():
        if filename.lower().startswith(prefix) and os.path.isfile(source_filepath):
            destination_filepath = os.path.join(destination, filename)
            shutil.move(source_filepath, destination_filepath)
            print(f"Moved '{filename}' to the {prefix.capitalize()} folder.")
            break  # Exit loop after moving the file to one folder

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    move_file(filename, source_directory)

print("File sorting completed.")
le)
            print(f"Moved {filename} from {dirName} to {destination}")

print("GateFees files moved to destination")
