# bitwise operator

def main():
    b(5)
    
def b(n):print('{:08b}'.format(n))
x, y = 0x55, 0xaa
b(x)
b(y)

b(x|y)
b(x & y)
b(x ^ y)
b(x ^ 0)
b(x ^ 0xff)
b(x << 4)
b(x >> 4)
b(~ x)


if __name__ == "__main__":
    main()
