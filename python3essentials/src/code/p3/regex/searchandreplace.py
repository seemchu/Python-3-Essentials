# regex example
import re 


def main():
    s = ''' this is first line
second line
this is third line
no data'''
    for i in s.splitlines():
        print(re.sub('(this|line)', '###', i))
    for i in s.splitlines():
        match = re.search('(this|line)', i)
        if match:
            print(i.replace(match.group(),"###"), end = ' ')
          
if __name__ =="__main__":
    main() 