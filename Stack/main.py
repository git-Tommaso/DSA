from Stack import Stack  # Import the Stack class

# Create a new stack with an initial value of 1
my_stack = Stack(1)

# Push values onto the stack
my_stack.push(2)  # Add 2 to the top
my_stack.push(3)  # Add 3 to the top
my_stack.push(4)  # Add 4 to the top
my_stack.push(5)  # Add 5 to the top

# Pop the top value from the stack
my_stack.pop()  # Remove the top value (5)

# Print the current stack
my_stack.print_stack()  # Output: 4, 3, 2, 1
