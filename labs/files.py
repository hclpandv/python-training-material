import os

path = "/etc"  # Replace with the directory to process
files = os.listdir(path)
file_count = len(files)

print(f"Files in {path}: {files}")
print(f"Total number of files: {file_count}")
