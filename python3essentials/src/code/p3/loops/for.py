# for loop
# lines.txt file is placed in the sample folder as for.py program
# for loop is desired to work with iterators

def main():
    fh = open("lines.txt")
    for line in fh.readlines():
        print(line, end="")

if __name__ == "__main__":
    main()