def factorial_for(n):
    fac = n
    for i in range(n-1):
        fac *= (n-1)
        n -= 1
    return fac


def factorial_while(n):
    fac = n
    while n>1:
        fac *= (n-1)
        n -= 1
    return fac


def digit_sum(n):
    digitSum = 0
    while n > 0:
        digitSum += n % 10
        n = n // 10
    return digitSum

def repeated_digit_sum(n):
    digitSum = digit_sum(n)
    if digitSum > 9:
        return repeated_digit_sum(digitSum)
    else:
        return digitSum


def divisors(n):
    print(1, end=", ")
    for i in range(2, n + 1):
        if n % i == 0:
            print(i, end=", ")
    print()

def divisors_count(n):
    count = 1
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
    return count


def is_prime(n):
    if divisors_count(n) == 2:
        return True
    else:
        return False


def primes_less_than(limit):
    for i in range(1, limit):
        if is_prime(i):
            print(i, end=", ")
    print()


def kth_prime(k):
    i = 2
    counter = 0
    while counter < k:
        if is_prime(i):
            counter += 1
        if counter == k:
            return i
        i += 1


def primes(count):
    counter = 0
    i = 2
    while counter < count:
        if is_prime(i):
            counter += 1
            print(i, end=", ")
        i += 1
    print()

def prime_twins(count):
    counter = 0
    i = 2
    while counter < count:
        if is_prime(i) and is_prime(i+2):
            counter += 1
            print("{}-{}".format(i, i+2), end=", ")
        i += 1
    print()


def factorization(n):
    i = 2
    while n > 1:
        if is_prime(i):
            if n % i == 0:
                print(i, end=", ")
                n = n // i
                i -= 1
        i += 1
    print()


def power_factorization(n):
    i = 2
    prime_list = []
    while n > 1:
        if is_prime(i):
            if n % i == 0:
                prime_list.append(i)
                n = n // i
                i -= 1
        i += 1
    last_printed = 0
    for p in prime_list:
        if p != last_printed:
            print("{}^{}".format(p, prime_list.count(p)), end=", ")
        last_printed = p

    print()


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b - a)


def factors(n):
    i = 2
    factors_list = []
    while n > 1:
        if is_prime(i):
            if n % i == 0:
                factors_list.append(i)
                n = n // i
                i -= 1
        i += 1
    return factors_list


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def euclid(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def e():
    n_fac = 1
    i = 1
    euler = 1
    while n_fac > 0.000001:
        n_fac /= i
        euler += n_fac
        i += 1
    return euler



def dec_to_x(n, symbols):
    x = len(symbols)
    converted = ""
    while n > 0:
        m = n % x
        converted += symbols[m]
        n //= x
    return converted[::-1]


"""
print(factorial_for(5))
print(factorial_while(5))
print(digit_sum(123456789))
print(repeated_digit_sum(123456789))
divisors(1024)
print(divisors_count(1024))
print(is_prime(101))
primes_less_than(100)
print(kth_prime(100))
primes(10)
prime_twins(10)
factorization(1024)
power_factorization(44)
print(gcd(5, 10))
print(lcm(360, 42))
print(euclid(42, 36))
"""
#print(dec_to_x(42, "0123456789"))
print(e())
