import os

def get_files_info(working_directory: str, directory: str) -> str:

    abs_path: str = os.path.abspath(working_directory) #get abs path from relative
    full_path: str = os.path.join(abs_path, directory) # normalize path / join two paths together
    norm_full_path: str = os.path.normpath(full_path)
#    print(f"Joined paths: {norm_full_path}")
    # check whether the full path falls within the working_directory
    common_path: str = os.path.commonpath([abs_path, norm_full_path])
#   print(f"Common path; {common_path}")
    valid_full_path: bool =  (common_path == abs_path)

#    print(f"Valid full path: {valid_full_path}")
    if(not valid_full_path):
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"        
    elif(not os.path.isdir(directory)):
        return f"Error: \"{directory}\" is not a directory"
    else:
        return f"Success: \"{directory}\" is within the working directory"


