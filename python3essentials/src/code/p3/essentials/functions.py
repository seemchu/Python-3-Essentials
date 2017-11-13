# Functions in Python


def func():
    for i in range(10):
        print(i, end="")
    print(">>>>>>")
   
def func(a =1):
    for a in range(a,10):
        print(a, end=" ")
    print(">>>>>>")
     

def main():
    func()
    func(6)
    func(3)

if __name__ == "__main__":
    main()
