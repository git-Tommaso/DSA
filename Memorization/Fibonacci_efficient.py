# Initialize memoization array to store computed Fibonacci values
memo = [None] * 100
# Counter to track the number of function calls
counter = 0

def fibonacci(n):
    """
    Calculates the nth Fibonacci number using memoization to avoid redundant calculations.
    This implementation is efficient because it stores previously computed values.
    
    Args:
        n (int): The position in the Fibonacci sequence
    Returns:
        int: The nth Fibonacci number
    Time Complexity: O(n) - linear time
    Space Complexity: O(n) - for memoization array
    """
    global counter
    counter += 1  # Increment counter for each function call

    # If value already computed, return it from memo
    if memo[n] is not None:
        return memo[n]

    # Base cases: F(0) = 0, F(1) = 1
    if n == 0 or n == 1:
        return n
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    # Store result in memo before returning
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Test with n = 10
n = 10
print("\nFibonacci of ", n, " = ", fibonacci(n))
print("\nCounter: ", counter)  # Shows how many times the function was called

# Test with n = 20
n = 20
print("\nFibonacci of ", n, " = ", fibonacci(n))
print("\nCounter: ", counter)  # Shows how many times the function was called

# Test with n = 30
n = 30
print("\nFibonacci of ", n, " = ", fibonacci(n))
print("\nCounter: ", counter)  # Shows how many times the function was called

"""
This implementation demonstrates the efficiency of memoization:
- Each Fibonacci number is calculated only once
- Subsequent calls use the stored value from memo
- The number of function calls grows linearly with n
- Much more efficient than the naive recursive approach
"""