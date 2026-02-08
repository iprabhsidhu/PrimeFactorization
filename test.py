'''
Test cases for Mixed_Sets

Case 1: Print all the sets from 16-100 (manual verification required)
Case 2: Check for solution on the following number : 3342 and 5466
Verifaction : no solution exists for 3342 and 5466

'''

from solver import find_solution_sets_same_prime

def test_case_1():
    for N in range(16, 33):
        sols = find_solution_sets_same_prime(N, max_factors=3)
        if sols:
            print(f"\nN = {N}: {len(sols)} solutions")
            for s in sols:
                print(f"  {' x '.join(s['factors'])} "
                    f"(prod={s['prod']}, units={s['units']}, diff={s['prod']-s['units']})")

def test_case_2() -> bool:
    number = [3342, 5466]
    for i in number:
        solution = find_solution_sets_same_prime(solution)
        if not solution:
            return True
    return False