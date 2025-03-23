#the first element is called root
root = {
   "value": 4,
   "left": None,
   "right": None
}

#every element can spit into two elements (Binary tree),
#but they can olso point to unlimited number of elements (Tree)

ROOT = { #<=PARENT
   "value": 4,
   "left": { #<=CHILD (they share the same parent, so they are siblings)
      "value": 3,
      "left": None, #<==LEAF (the bottom elements are called leaves)
      "right": None #<==LEAF
   },
   "right": { #<=CHILD
      "value": 23,
      "left": None, #<==LEAF
      "right": None #<==LEAF
   }
}

#this is a full tree because every element has two children
#and is also a perfect tree because all the leaves are at the same level
#and is complete, because all the levels are full (with no gaps)

#big 0 notation
#insertion: O(log n)
#search: O(log n)
#deletion: O(log n)