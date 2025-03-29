from Queue import Queue  # Import the Queue class

# Create a new queue with an initial value of 1
my_queue = Queue(1)

# Enqueue values into the queue
for i in range(2, 10, 1):  # Add values from 2 to 9
   my_queue.Enqueue(i)

print("my list before Dequeue")  # Print the queue before dequeuing
my_queue.print_queue()

# Dequeue values until only one node remains
while my_queue.length > 1:
   my_queue.Dequeue()

print("my list after Dequeue")  # Print the queue after dequeuing
my_queue.print_queue()