# Counter to track the number of function calls
counter = 0

def fibonacci(n):
    """
    Calculates the nth Fibonacci number using a naive recursive approach.
    This implementation is inefficient because it recalculates the same values multiple times.
    
    Args:
        n (int): The position in the Fibonacci sequence
    Returns:
        int: The nth Fibonacci number
    Time Complexity: O(2^n) - exponential time
    Space Complexity: O(n) - depth of recursion tree
    """
    global counter
    counter += 1  # Increment counter for each function call
    
    # Base cases: F(0) = 0, F(1) = 1
    if n == 0 or n == 1:
        return n
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test with n = 10
n = 10
print("\nFibonacci of ", n, " = ", fibonacci(n))
print("\nCounter: ", counter)  # Shows how many times the function was called

# Test with n = 20
n = 20
print("\nFibonacci of ", n, " = ", fibonacci(n))
print("\nCounter: ", counter)  # Shows how many times the function was called

"""
This implementation demonstrates the inefficiency of naive recursion for Fibonacci:
- For n=10, the function is called 177 times
- For n=20, the function is called 21,891 times
- The number of calls grows exponentially with n
- Many values are recalculated multiple times
"""