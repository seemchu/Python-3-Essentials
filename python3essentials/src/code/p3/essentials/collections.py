# Example for list, Tuple, directories

def main():
    varTuple = (1, 2, 3)
    varList = [1, 2, 3]
    varList.insert(2, 4)
    varList.append(5)
    print (type(varTuple),varTuple)
    print (type(varList),varList)
    print (varList[2])
    print (varList[2:5])
    
    for i in varTuple:
        print(i)
 
def dictfun():  
    d = {"one" : 1,"two" : 2,"three" : 3}
    d['four'] = 7
    for k in sorted(d.keys()):
        print(k,d[k])
     
    
if __name__ == "__main__":
    main()
    dictfun()