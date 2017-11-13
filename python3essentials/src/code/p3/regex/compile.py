# regex compile
import re
def main():
    s = ''' this is first line
second line
this is third line
no data'''
    pattern =re.compile('(this|line)', re.IGNORECASE)
    for i in s.splitlines():
        if re.search(pattern, i):
            print(re.sub('(this|line)', '###', i))
              
if __name__ =="__main__":
    main() 