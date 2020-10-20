def sqrt(x):
    return x**(1/2)
def floor(x):
    return int(x)
def product(lst):
    '''
    returns the product of all the elements in a list.
    '''
    p = 1
    for x in lst:
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
        """
        Checks if a number is prime
        """
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
        """
        Lists primes between two numbers.
        """
        primes = []
        for i in range(start, stop+1):
            number = check(i)
            if number == 1:
                primes.append(i)
        return primes
    def num_primes(start=1, stop=100):
        """
        Say how many primes are between two numbers
        """
        primes = []
        for i in range(start, stop+1):
            number = check(i)
            if number == 1:
                primes.append(i)
        return len(primes)

    def number(number):
        """
        Says the xth prime
        """
        x = number+1
        primes = listprime(stop = x)
        while len(primes) < number:
            x += 1
            primes = listprime(stop = x)
        return primes[number-1]
