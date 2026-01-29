# Sets of Factorization
(idk what is the title)
Module to solve the prime power product equation:
    Π(p_i^a_i) - Π(p_i^a_i - 1) = m
where the product of prime powers is bounded by m^2.

# How to run
```python
    python main.py
```

# Examples
following are the examples of program
```cmd
Enter the number >>> 1000
[(2, 2), (19, 1), (43, 1)]
[(2, 2), (997, 1)]
[(2, 3), (3, 2), (59, 1)]
[(2, 3), (3, 4), (5, 1)]
[(2, 3), (17, 1), (37, 1)]
[(2, 4), (5, 1), (47, 1)]
[(2, 6), (5, 1), (11, 1)]
[(2, 6), (937, 1)]
```
```cmd
Enter the number >>> 900
[(2, 2), (3, 1), (149, 1)]
[(2, 2), (3, 2), (73, 1)]
[(2, 7), (773, 1)]
[(2, 9), (389, 1)]
```

# Find_prime_set
Finds all sets of prime-power pairs (p_i, a_i) satisfying the difference equation.
    
The function uses a recursive Depth-First Search (DFS) to explore potential 
prime combinations whose product of powers is less than m^2.

Args:
    m (int): The target difference value.
Returns:
    list[list[tuple[int, int]]]: A list of solutions, where each solution is a list of (prime, exponent) tuples.

# dfs_prime

Recursive helper to explore prime combinations.
    Args:
        start_idx (int): Current index in the primes list to avoid duplicate sets.
        A (int): Current product of p_i^a_i.
        B (int): Current product of (p_i^a_i - 1).
        current (list): Accumulated list of (p_i, a_i) pairs for the current path.

# utils.py
This is a utility module coded with functions like is_prime(n) and primerange(lower,upper).
