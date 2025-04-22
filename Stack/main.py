from Stack import Stack  # Import the Stack class

# Create a new stack with an initial value of 1
# This initializes the stack with one node at the top
my_stack = Stack(1)

# Push values onto the stack
# This demonstrates the LIFO (Last-In-First-Out) property of stacks
# Values are added to the top of the stack
my_stack.push(2)  # Add 2 to the top (stack: 2 -> 1)
my_stack.push(3)  # Add 3 to the top (stack: 3 -> 2 -> 1)
my_stack.push(4)  # Add 4 to the top (stack: 4 -> 3 -> 2 -> 1)
my_stack.push(5)  # Add 5 to the top (stack: 5 -> 4 -> 3 -> 2 -> 1)

# Pop the top value from the stack
# This removes the most recently added value (5)
my_stack.pop()  # Remove the top value (stack: 4 -> 3 -> 2 -> 1)

# Print the current stack
# This shows the remaining values in the stack from top to bottom
my_stack.print_stack()  # Output: 4, 3, 2, 1
