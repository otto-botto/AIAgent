from functions.write_file import write_file


def main():
    cases: [str] = ["lorem.txt", "pkg/morelorem.txt", "/tmp/temp.txt"]
    content: [str] = ["wait, this isn't lorem ipsum", "lorem ipsum dolor sit amet", "this should not be allowed"]
    count: int = 0
    while(count < 3):
        print(write_file("calculator", cases[count], content[count]))
        count+=1



if __name__=='__main__':
    main()
