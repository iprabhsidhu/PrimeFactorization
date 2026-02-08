# Ring Non‑Unit Invariant Enumerator

This project searches for finite commutative rings (built from prime‑power components) whose **number of non‑units** equals a given integer `N`.

The program checks the invariant:

```
N = |R| − |U(R)|
```

where

* `|R|` = total number of elements in the ring
* `|U(R)|` = number of invertible elements (units)

---

## Allowed building blocks

Each factor in a product can be one of two types.

### Finite field

`F(p^a)`  (printed as `F8`, `F9`, etc.)

Properties:

* number of elements: `p^a`
* number of units: `p^a − 1`

All non‑zero elements are invertible.

---

### Prime‑power residue ring

`Z(p^a)`  (printed as `Z4`, `Z8`, etc.)

This means integers modulo `p^a`.

Properties:

* number of elements: `p^a`
* number of units: `p^a − p^(a−1)`

These rings contain zero divisors and nilpotent elements.

---

## Product rings

The program constructs rings of the form:

```
R = R1 × R2 × ... × Rk
```

For such a product:

```
|R|     = product of (p_i^a_i)
|U(R)|  = product of the unit counts of each component
```

A decomposition is accepted if:

```
|R| − |U(R)| = N
```

This value is exactly the number of **non‑invertible elements** in the ring.

---

## Same‑prime decompositions

The solver allows repeated primes. Examples that can appear:

* `F8 × Z4`
* `Z8 × Z4`
* `F2 × F2 × F5`

This is intentional. The search is not restricted by the Chinese Remainder Theorem; it simply checks the invariant equation.

---

## Installation

Requirements:

* Python 3.9+
* sympy

Install dependency:

```bash
pip install sympy
```

---

## Running

Example usage in Python:

```python
from solver import find_solution_sets_same_prime

solutions = find_solution_sets_same_prime(18)
for s in solutions:
    print(s)
```

Or print a range:

```python
pretty_print_solutions(16, 33)
```

---

## Output format

Example line:

```
F8 x Z4  (prod=32, units=14, diff=18)
```

Meaning:

* `F8` : finite field of size 8 (2^3)
* `Z4` : integers modulo 4
* `prod` : total elements |R|
* `units` : number of invertible elements |U(R)|
* `diff` : |R| − |U(R)|

---

## Why duplicates appear

You may see:

```
F2 x F4 x F3
F4 x F2 x F3
```

These represent the same algebraic structure but different construction orders. The search space is ordered tuples, while direct products are commutative up to isomorphism.

So duplicates are **expected** and do not indicate an error.

---

## Configuration

Key parameter:

```
max_factors
```

Controls the maximum number of components in a product ring.

| max_factors | Behavior  |
| ----------- | --------- |
| 2           | fast      |
| 3           | practical |
| 4+          | very slow |

---

## Performance notes

The search is combinatorial. Runtime increases quickly because it explores:

* all primes ≤ N
* all exponents satisfying p^(a−1) ≤ N
* both ring types
* all product combinations

Large `N` will be slow without pruning.

---

## What the results mean

The program answers:

> In how many ways can a product of allowed components have exactly N non‑invertible elements?

It does **not** classify all finite rings.

---

## Limitations

* Counts include permutations of factors
* Not a complete classification of rings
* Runtime grows quickly for large N
* Only the listed ring types are considered

---

## Possible extensions

* Canonical isomorphism collapsing (remove duplicates)
* Parallel search
* Export results to CSV/JSON

---
