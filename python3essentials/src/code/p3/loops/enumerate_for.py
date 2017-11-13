# for loop with enumerate to get the index
# lines.txt file is placed in the sample folder as for.py program

def main():
    fh = open("lines.txt")
    for index,line in enumerate(fh.readlines()):
        print(index, line, end="")
    s = "hello world"
    print()
    for i, c in enumerate(s):
        if c =='o': print("index of o {}".format(i))

if __name__ == "__main__":
    main()