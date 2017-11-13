# Objects syntax in python-essentionals 3

class Egg:
    def __init__(self,kind = "fried"):
        self.kind = kind
    def whatkind(self):
        return self.kind  
def main():
    fried=Egg()
    scrambled =Egg("Scrambled")
    print(fried.whatkind())
    print(scrambled.whatkind())
    

if __name__ == "__main__":
    main()

