"""
Module to solve the prime power product equation:

    Π(p_k^a_k) - Π(p_k^a_k - p_k^(a_k - 1)) = m

Constraints:
    Π(p_k^a_k) < m^2
    m < 2^i - 1, where i is the smallest integer satisfying the condition
"""

from utils import primerange
import math


def smallest_i(m):
    """Find smallest i such that m < 2^i - 1"""
    i = 1
    while (2 ** i - 1) <= m:
        i += 1
    return i


def find_prime_sets(m):
    lim = m * m
    primes = list(primerange(2, m + 2))
    solutions = []

    max_depth = smallest_i(m)

    def dfs_prime(start_idx, A, B, current):
        # product bound
        if A >= lim:
            return

        # depth bound from 2^i - 1
        if len(current) > max_depth:
            return

        # check equation
        if current and A - B == m:
            solutions.append(current.copy())
            # do not return; supersets might also work

        for i in range(start_idx, len(primes)):
            p = primes[i]
            p_power = p
            a = 1

            while True:
                newA = A * p_power
                if newA >= lim:
                    break

                # p^a - p^(a-1) = p^(a-1)(p-1)
                term = (p_power // p) * (p - 1)
                newB = B * term

                dfs_prime(
                    i + 1,          # strictly increasing primes
                    newA,
                    newB,
                    current + [(p, a)]
                )

                p_power *= p
                a += 1

    dfs_prime(0, 1, 1, [])
    return solutions


if __name__ == "__main__":
    for i in range(16, 51):
        print('-----------------------------')
        print(f'current number : {i}')
        sols = find_prime_sets(i)

        if not sols:
            print("No solutions found.")
        else:
            for s in sols:
                print(s)
