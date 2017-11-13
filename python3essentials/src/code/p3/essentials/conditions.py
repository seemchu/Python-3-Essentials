# Conditions: selecting the code and values with conditions

def main():
    a, b = 0, 1
    if a < b:
        print(" {} is less than {}".format(a, b))
    elif a == b:
       print(" {} is equal to {}".format(a, b)) 
    else:
        print(" {} is greater than {}".format(a, b))
 
    s = "less than" if a < b else "not less than"
    print(s) 
    
   

    
    
if __name__ == "__main__":
    main()
    

    