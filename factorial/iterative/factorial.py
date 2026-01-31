# factorial.py
# iterative version

def factorial(n: int) -> int:
    result = 1

    # iterate through n, multiply each time
    for i in range(n, 1, -1):
        result *= i

    return result

# Tests
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(10) == 3_628_800