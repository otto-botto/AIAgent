from functions.get_file_content import get_file_content

def main():
    cases: str = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

    for case in cases:
        
        result = get_file_content("calculator", case)
        if (case == "lorem.txt"):
            result = get_file_content("calculator", "lorem.txt")
            print(f"lorem.txt length: {len(result)}")
            print(f"lorem.txt truncated: {'truncated' in result}")
        else:
            print(result)
        


if __name__ == '__main__':
    main()
