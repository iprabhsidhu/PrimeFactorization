"""
Module to solve the prime power product equation:
    Π(p_i^a_i) - Π(p_i^a_i - 1) = m
where the product of prime powers is bounded by m^2.
"""

from utils import primerange, GIN

def find_prime_sets(m):
    lim = m * m
    # Generate potential primes up to m+1 to cover potential factors
    primes = list(primerange(2, GIN(m/2)+2))
    solutions = []

    def dfs_prime(start_idx, A, B, current):
        # Base Case: Stop if product exceeds the limit m^2
        if A >= lim:
            return

        # Check if the current combination satisfies the equation: A - B = m
        if current and A - B == m:
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

                # Recurse with the next prime index to ensure strictly increasing prime sets
                dfs_prime(
                    i,
                    newA,
                    newB,
                    current + [(p, a)]
                )

                # Increment power: p^1 -> p^2 -> p^3...
                p_power *= p
                a += 1

    # Start recursion with initial products A=1, B=1
    dfs_prime(0, 1, 1, [])
    return solutions

if __name__ == "__main__":
    try:
        for i in range(16, 51):
            print('-----------------------------')
            print(f'current number : {i}')
            Solutions = find_prime_sets(i)
        
            if not Solutions:
                print("No solutions found.")
            for s in Solutions:
                print(s)
    except ValueError:
        print("Please enter a valid integer.")