# While loop example

def main():
    a, b=0, 1
    while b < 150:
        print (b, end = ' ')
        a, b = b, a + b
    print()
    loopfunc()
# break, continue, else in while loop

def loopfunc():
    s = "Besto Python"
    for c in s:
        if c == "o":
            continue
        elif c == "P":
            break        
        print (c, end=" ")
    else:
        print("end of iterator") 
    

if __name__ == "__main__":
    main()
    
    