from Queue import Queue  # Import the Queue class

# Create a new queue with an initial value of 1
# This initializes the queue with one node, setting both first and last to this node
my_queue = Queue(1)

# Enqueue values into the queue
# This demonstrates the FIFO (First-In-First-Out) property of queues
# Values are added to the end (rear) of the queue
for i in range(2, 10, 1):  # Add values from 2 to 9
    my_queue.Enqueue(i)

# Print the queue before any dequeuing operations
# This shows the initial state of the queue with all values
print("my list before Dequeue")
my_queue.print_queue()

# Dequeue values until only one node remains
# This demonstrates removing elements from the front of the queue
while my_queue.length > 1:
    my_queue.Dequeue()

# Print the queue after dequeuing operations
# This shows the final state of the queue with only one value remaining
print("my list after Dequeue")
my_queue.print_queue()