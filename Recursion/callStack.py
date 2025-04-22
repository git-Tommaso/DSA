def funcThree():
    """
    The innermost function in the call stack.
    Prints "Three" and returns to funcTwo.
    """
    print("Three")

def funcTwo():
    """
    The middle function in the call stack.
    Calls funcThree, waits for it to complete, then prints "Two".
    """
    funcThree()  # Call funcThree
    print("Two")  # Execute after funcThree returns

def funcOne():
    """
    The outermost function in the call stack.
    Calls funcTwo, waits for it to complete, then prints "One".
    """
    funcTwo()  # Call funcTwo
    print("One")  # Execute after funcTwo returns

# Start the chain of function calls
# This demonstrates how the call stack works in Python
funcOne()

"""
Example of the call stack execution:
1. funcOne is called
2. funcOne calls funcTwo
3. funcTwo calls funcThree
4. funcThree prints "Three" and returns
5. funcTwo prints "Two" and returns
6. funcOne prints "One" and returns

Expected output:
Three
Two
One

This demonstrates the Last-In-First-Out (LIFO) nature of the call stack,
where the most recently called function is the first to complete.
"""