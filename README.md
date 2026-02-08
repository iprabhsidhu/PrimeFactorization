# Ring Non‑Unit Invariant Enumerator

This project searches for finite commutative rings (built from prime–power components) whose **number of non‑units** equals a given integer `N`.

Formally, for a ring `R`, the program finds decompositions satisfying:

[
N = |R| - |U(R)|
]

where:

* `|R|` = total number of elements in the ring
* `|U(R)|` = number of invertible elements (units)

The solver enumerates products of finite fields and prime‑power residue rings and checks this invariant exactly.

---

## Mathematical Background

The program constructs rings as direct products:

[
R = R_1 \times R_2 \times \cdots \times R_k
]

Each component is one of the following.

### 1. Finite Fields

[
F_{p^a}
]

Properties:

| Quantity | Value     |
| -------- | --------- |
| Elements | (p^a)     |
| Units    | (p^a - 1) |

All non‑zero elements are invertible.

---

### 2. Prime‑Power Residue Rings

[
\mathbb{Z}/p^a\mathbb{Z}
]
(denoted `Z(p^a)` in the output)

Properties:

| Quantity | Value           |
| -------- | --------------- |
| Elements | (p^a)           |
| Units    | (p^a - p^{a-1}) |

These rings contain nilpotent elements and zero divisors.

---

## Invariant Being Solved

For a product ring:

[
R = \prod_{i=1}^{k} R_i
]

we have:

### Total elements

[
|R| = \prod_{i=1}^{k} p_i^{a_i}
]

### Total units

[
|U(R)| =
\prod_{i \in \text{fields}} (p_i^{a_i}-1)
\cdot
\prod_{i \in Z} (p_i^{a_i}-p_i^{a_i-1})
]

The program keeps a decomposition if:

[
\boxed{|R| - |U(R)| = N}
]

This value equals the number of **non‑invertible elements** of the ring.

---

## What the Program Enumerates

The solver now allows **same‑prime decompositions**. Examples:

* `F8 × Z4`
* `Z8 × Z4`
* `F2 × F2 × F5`

These are not restricted by the Chinese Remainder Theorem; the search is purely based on satisfying the invariant equation.

Important: the program enumerates **constructions**, not unique rings. The same structure may appear in multiple orders.

---

## Installation

Requirements:

* Python 3.9+
* `sympy`

Install dependency:

```bash
pip install sympy
```

---

## Running

Typical usage:

```python
from solver import find_solution_sets_same_prime

solutions = find_solution_sets_same_prime(18)
for s in solutions:
    print(s)
```

Or using the provided range printer:

```python
pretty_print_solutions(16, 33)
```

---

## Output Format

Example line:

```
F8 x Z4  (prod=32, units=14, diff=18)
```

Meaning:

| Field   | Meaning                      |      |   |      |   |
| ------- | ---------------------------- | ---- | - | ---- | - |
| `F8`    | finite field of order 8 (2³) |      |   |      |   |
| `Z4`    | integers mod 4               |      |   |      |   |
| `prod`  | total elements (             | R    | ) |      |   |
| `units` | invertible elements (        | U(R) | ) |      |   |
| `diff`  | non‑units count = `          | R    | - | U(R) | ` |

---

## Why Duplicates Appear

You may see:

```
F2 x F4 x F3
F4 x F2 x F3
```

These represent the same algebraic structure but different construction orders. The search space is ordered tuples, while direct products are commutative up to isomorphism.

If unique structures are required, canonicalization (sorting factors) must be applied before storing results.

---

## Configuration

Key parameter:

```
max_factors
```

Controls the maximum number of components in a product ring.

Higher values:

* Find more solutions
* Increase runtime exponentially

Recommended values:

| max_factors | Behavior  |
| ----------- | --------- |
| 2           | fast      |
| 3           | practical |
| 4+          | very slow |

---

## Performance Notes

The search is combinatorial. Complexity grows rapidly because it explores:

* all primes ≤ N
* all exponents satisfying p^(a−1) ≤ N
* both ring types
* all product combinations

Large `N` will become slow without pruning or caching.

---

## Interpretation of Results

The program does **not classify rings**. It solves an arithmetic condition.

The table answers:

> In how many ways can a product of prime‑power components have exactly `N` non‑invertible elements?

It does **not** answer:

> How many distinct rings exist?

Those are different mathematical problems.

---

## Limitations

* Counts include permutations of factors
* Not a complete classification of finite rings
* Runtime grows quickly for large N
* Only commutative rings of the listed forms are considered

---

## Possible Extensions

* Canonical isomorphism collapsing
* Parallel search
* Analytical characterization of solvable N
* Export to CSV/JSON

---

## License

Specify your license here (MIT recommended).
