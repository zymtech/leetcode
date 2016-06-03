# coding: uft-8

"""
Goldbach Conjecture
"""


def divisors(n):
    return [x for x in range(1,n+1) if n % x ==0]


def is_prime(n):
    return divisors(n) == [1,n]


def prime_range(n):
    return [x for x in range(2,n+1) if is_prime(x)]


def goldbach_conjecture(n):
    if n%2==0:
        if n>2:
            return [(x,y) for x in prime_range(n) for y in prime_range(n) if x+y==n and x<=y]
        else:
            return None
    else:
        return None

def solution(n):
    for i in range(n):
        results = goldbach_conjecture(i)
        if results:
            for result in results:
                print i, "=", result[0], "+", result[1]


if __name__ == '__main__':
    solution(2000)