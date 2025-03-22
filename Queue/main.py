from Queue import Queue

my_queue = Queue(1)

for i in range(2,10,1):
   my_queue.Enqueue(i)

print("my list before Dequeue")
my_queue.print_queue()

while my_queue.length > 1:
   my_queue.Dequeue()

print("my list after Dequeue")
my_queue.print_queue()