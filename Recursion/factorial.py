def factorial(n):
    """
    Calculates the factorial of a number using recursion.
    Factorial of n (n!) is the product of all positive integers less than or equal to n.
    
    Args:
        n (int): The number to calculate factorial for
    Returns:
        int: The factorial of n
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursive call stack
    """
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)
   
# Test the factorial function with n = 4
# Expected output: 24 (4! = 4 * 3 * 2 * 1)
print(factorial(4))

"""
Example of how the recursion works for factorial(4):
4! = 4 * 3!
   3! = 3 * 2!
      2! = 2 * 1!
         1! = 1 (base case)
      2! = 2 * 1 = 2
   3! = 3 * 2 = 6
4! = 4 * 6 = 24
"""