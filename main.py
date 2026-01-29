"""
Module to solve the prime power product equation:
    Π(p_i^a_i) - Π(p_i^a_i - 1) = m
where the product of prime powers is bounded by m^2.
"""

from utils import primerange

def find_prime_sets(m):
    """
    Finds all sets of prime-power pairs (p_i, a_i) satisfying the difference equation.
    
    The function uses a recursive Depth-First Search (DFS) to explore potential 
    prime combinations whose product of powers is less than m^2.

    Args:
        m (int): The target difference value.

    Returns:
        list[list[tuple[int, int]]]: A list of solutions, where each solution 
            is a list of (prime, exponent) tuples.
    """
    lim = m * m
    # Generate potential primes up to m+1 to cover potential factors
    primes = list(primerange(2, m + 2))
    solutions = []

    def dfs_prime(start_idx, A, B, current):
        """
        Recursive helper to explore prime combinations.

        Args:
            start_idx (int): Current index in the primes list to avoid duplicate sets.
            A (int): Current product of p_i^a_i.
            B (int): Current product of (p_i^a_i - 1).
            current (list): Accumulated list of (p_i, a_i) pairs for the current path.
        """
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
                    i + 1,
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
    # Input handling and execution
    try:
        number = int(input('Enter the number >>> '))
        Solutions = find_prime_sets(number)
        
        if not Solutions:
            print("No solutions found.")
        for s in Solutions:
            print(s)
    except ValueError:
        print("Please enter a valid integer.")