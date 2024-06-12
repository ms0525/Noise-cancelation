import os
def rename_files(folder_path):
    i=0
    # Iterate over the files in the folder
    for filename in os.listdir(folder_path):
        new_name = filename.replace(filename, str(i)+'.jpg')  # Replace the old name with the new name pattern
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_name)
        os.rename(old_file_path, new_file_path)  # Rename the file
        i+=1