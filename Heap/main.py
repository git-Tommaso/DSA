from MaxHeap import MaxHeap

myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)  

myheap.insert(100)
print(myheap.heap) 

myheap.insert(75)
print(myheap.heap) 


"""
   EXPECTED OUTPUT:
   ----------------------
   [99, 72, 61, 58]
   [100, 99, 61, 58, 72]
   [100, 99, 75, 58, 72, 61]

"""