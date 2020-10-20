def sqrt(x):
    return x**(1/2)
def floor(x):
    return int(x)
def product(l):
    p = 1
    for x in l:
        p = p*x
    return p
class factor:
    def LCM(a, b):
        for i in range(max([a,b]), a*b+1):
            if i%a == 0 and i%b == 0:
                return i
    def GCD(a, b):
        for i in range(1, a*b+1):
            if a%i == 0 and b%1 == 0:
                return i
    def factorize(a):
        f = []
        for i in range(1, a+1):
            if a%i == 0:
                f.append(i)
        return f
class prime:
    primes = []
    def check(number):
        number = int(number)
        if number <= 1:
            return "Not prime or composite"
        if number == 2:
            return 1
        if number%2 == 0:
            return 2
        for i in range(3, floor(sqrt(number))+1, 2):
            if number%i == 0:
                return i
        return 1

    def listprime(start=1, stop=100):
        primes = []
        for i in range(start, stop+1):
            number = prime.check(i)
            if number == 1:
                primes.append(i)
        return primes
    def num_primes(start=1, stop=100):
        primes = []
        for i in range(start, stop+1):
            number = prime.check(i)
            if number == 1:
                primes.append(i)
        return len(primes)
        
    def number(number):
        x = number+1
        primes = prime.listprime(stop = x)
        while len(primes) < number:
            x += 1
            primes = prime.listprime(stop = x)
        return primes[number-1]
if __name__ == "__main__":
    print(factor.LCM(3,4))
    print(factor.GCD(3,4))
    print(factor.factorize(12))
    print(prime.check(203))
    print(prime.listprime(1, 100))
