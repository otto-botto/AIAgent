import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    abs_wkng_path: str = os.path.abspath(working_directory)
    full_path: str = os.path.join(abs_wkng_path, file_path)
    norm_full_path: str = os.path.normpath(full_path)
    

    # now ready to use the normalized dir to check whether in working dir
    common_path: str = os.path.commonpath([abs_wkng_path, norm_full_path])

    if (common_path != abs_wkng_path):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

    elif (not os.path.isfile(norm_full_path)):
        print(norm_full_path)
        return f"Error: File not found or is not a regular file: \"{file_path}\""
    else:
        with open(norm_full_path, "r") as f:
            content: str = f.read(MAX_CHARS)
        # is the file's content within 10K chars, read one more char
            if f.read(1):
                content += f" [... File '{file_path}' truncated at {MAX_CHARS} characters]"

        return content





#def main():
#    print(get_file_content("calculator", "main.py"))
#    print(get_file_content("calculator", "pkg/calculator.py"))
#    print(get_file_content("calculator", "/bin/cat"))
#    print(get_file_content("calculator", "pkg/does_not_exist.py"))


#if __name__ == '__main__':
#    main()
