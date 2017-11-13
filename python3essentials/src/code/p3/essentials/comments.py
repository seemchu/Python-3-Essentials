# This is the function prime

def main():
    for n in primes():
        if n > 100: break
        print(n)


def isprime(n):
    if n == 1: # one is never prime
        return False
    for x in range(2, n):
        if n % x == 0:
            return False # Found a divisor, not prime
    else:
        return True

def primes(n = 1):
    while True:
        if isprime(n): yield n # yield used as generator
        n += 1
        
if __name__ == "__main__":
    main()
        
        