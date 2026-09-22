import os

def get_files_info(working_directory: str, directory: str) -> str:

    try:

        abs_path: str = os.path.abspath(working_directory) #get abs path from relative
        full_path: str = os.path.join(abs_path, directory) # normalize path / join two paths together
        norm_full_path: str = os.path.normpath(full_path)
        common_path: str = os.path.commonpath([abs_path, norm_full_path])
        valid_full_path: bool =  (common_path == abs_path)

        if(not valid_full_path):
            return f"   Error: Cannot list \"{directory}\" as it is outside the permitted working directory"        
        elif(not os.path.isdir(norm_full_path)):
            return f"   Error: \"{directory}\" is not a directory"
        else:
            composite_list: [str] = []
            for item in os.listdir(norm_full_path):
                name: str = item
                #print(os.path.join(norm_full_path, item))
                size: int = os.path.getsize(os.path.join(norm_full_path,item))
                is_dir: Bool = os.path.isdir(os.path.join(norm_full_path, item))
                composite_str: str = f"  - {name}: file_size={size} bytes, is_dir={is_dir} "
                composite_list.append(composite_str)
        
            return_string: str = "\n".join(composite_list)

            return return_string
    except Exception as e:
        return f"Error: listing files {e}"


