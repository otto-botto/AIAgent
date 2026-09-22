from functions.get_files_info import get_files_info

def main():
    cases: [str] = [".", "pkg", "/bin", "../"]
    for item in cases:
        name: str = item
        if (name == ".") :
           name = "current"
           print(f"Result for {name} directory:")
        else:
           print(f"Result for '{name}' directory:")

        print(get_files_info("calculator", item))



if __name__ == '__main__':
    main()
