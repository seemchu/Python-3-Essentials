# Example for Slicers

def main():
    l = [1,2,3,4,5,6,7,8,9,10]
    print(l[0])
    print(l[0:9])
    print(l[0:10])
    for i in l[0:10:3]:
        print(i)

if __name__ == "__main__":
    main()