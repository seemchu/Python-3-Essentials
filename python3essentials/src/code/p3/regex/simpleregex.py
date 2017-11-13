# regex example
import re 


def main():
    s = ''' this is first line
second line
this is third line
no data'''
    for i in s.splitlines():
        if re.search('(this|line)', i):
            print(i)
    for i in s.splitlines():
        match = re.search('(this|line)', i)
        if match:
            print(match.group())

if __name__ =="__main__":
    main() 