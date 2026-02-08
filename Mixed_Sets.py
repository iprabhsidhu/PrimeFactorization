import sympy as sp
from itertools import product

def max_exponent_for_p(N, p):
    a = 1
    while p**(a-1) <= N:
        a += 1
    return a - 1

def find_solution_sets_same_prime(N, max_factors=3):
    solutions = []
    seen = set()

    primes = list(sp.primerange(2, N + 2))

    for k in range(1, max_factors + 1):

        for prime_tuple in product(primes, repeat=k):
            prime_tuple = tuple(sorted(prime_tuple))  # avoid permutations

            a_ranges = [range(1, max_exponent_for_p(N, p) + 1) for p in prime_tuple]

            for a_vals in product(*a_ranges):
                for ring_mask in product([0, 1], repeat=k):
                    # skip Z(p^1)
                    if any(a == 1 and r == 1 for a, r in zip(a_vals, ring_mask)):
                        continue

                    prod_orders = 1
                    prod_units = 1
                    factors = []

                    for p, a, r in zip(prime_tuple, a_vals, ring_mask):
                        order = p**a
                        prod_orders *= order

                        if r == 0:  # field
                            units = p**a - 1
                            factors.append(f"F{order}")
                        else:       # Z_p^a
                            units = p**a - p**(a-1)
                            factors.append(f"Z{order}")

                        prod_units *= units

                    if prod_orders - prod_units == N:
                        key = (tuple(factors), prod_orders)
                        if key not in seen:
                            seen.add(key)
                            solutions.append({
                                "factors": factors,
                                "prod": prod_orders,
                                "units": prod_units
                            })

    return solutions