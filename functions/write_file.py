import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_wkng_path: str = os.path.abspath(working_directory)
    full_file_path: str = os.path.join(abs_wkng_path, file_path)
    norm_file_path: str = os.path.normpath(full_file_path)

    common_path: str = os.path.commonpath([abs_wkng_path, norm_file_path])
    if (common_path != abs_wkng_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if (os.path.isdir(norm_file_path)):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(os.path.dirname(norm_file_path), exist_ok=True)

    with open(norm_file_path, "w") as f:
        chars_written: int = f.write(content)
        return f'Successfully wrote to "{file_path}" ({chars_written} characters written)'
    

        

    


#def main():
#    print(write_file("../calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#    print(write_file("../calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#    print(write_file("../calculator", "tmp/temp.txt", "this should not be allowed"))



#if __name__=='__main__':
    main()
