# factorial.py
# iterative version

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:    
        return n * factorial(n-1)

# Tests
print("Factorial(4) == 24: ", factorial(4))
assert factorial(4) == 24
print("Factorial(5) == 120: ", factorial(5))
assert factorial(5) == 120
print("Factorial(10) == 3628800:", factorial(10))
assert factorial(10) == 3_628_800