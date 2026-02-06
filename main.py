"""
Module to solve the prime power product equation:
    Π(p_i^a_i) - Π(p_i^a_i - 1) = m
where the product of prime powers is bounded by m^2.
"""

from utils import primerange, GIN, F
from math import prod

def solution_to_R(sol):
    sizes = [p**a for p, a in sol]        # field sizes
    return " × ".join(F(n) for n in sizes), prod(sizes)

def find_prime_sets(m):
    lim = m * m
    # Generate potential primes up to m+1 to cover potential factors
    primes = list(primerange(2, m+2))
    solutions = []

    def dfs_prime(start_idx, A, B, C, current):
        # Base Case: Stop if product exceeds the limit m^2
        if A >= lim:
            return

        # Check if the current combination satisfies the equation: A - B = m
        if current and C*(A - B) == m:
            solutions.append(current.copy())

        # Iteratively pick the next prime to maintain unique combinations (combinations, not permutations)
        for i in range(start_idx, len(primes)):
            p = primes[i]
            p_power = p
            a = 1

            # Explore all possible powers of the chosen prime 'p'
            while True:
                newA = A * p_power
                if newA >= lim:
                    break

                newB = B * (p_power - 1)
                newC = C * (p_power // p)

                # Recurse with the next prime index to ensure strictly increasing prime sets
                dfs_prime(
                    i,
                    newA,
                    newB,
                    newC,
                    current + [(p, a)]
                )

                # Increment power: p^1 -> p^2 -> p^3...
                p_power *= p
                a += 1

    # Start recursion with initial products A=1, B=1
    dfs_prime(0, 1, 1, 1,[])
    return solutions

import pandas as pd

def build_grouped_table(m_max=100):
    rows = []

    for m in range(16, m_max + 1):
        sols = find_prime_sets(m)
        if not sols:
            continue

        first = True
        for sol in sols:
            R_str, card = solution_to_R(sol)
            rows.append({
                "m": m if first else "",
                "R": R_str,
                "|R|": card
            })
            first = False

    return pd.DataFrame(rows)


if __name__ == "__main__":
    try:
        number = int(input('Enter the number :'))
        solution = find_prime_sets(number)
        print(solution)


        
    except ValueError:
        print("Please enter a valid integer.")