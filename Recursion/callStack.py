def funcThree():
   print("Three")

def funcTwo():
   funcThree()
   print("Two")

def funcOne():
   funcTwo()
   print("One")

funcOne()

"""
The code defines three functions: funcThree, funcTwo, and funcOne. Each function prints its name and calls the next function in the sequence. When funcOne is called, it triggers a chain of function calls that results in all three functions being executed in order.
The output of this code will be:
- Three
- Two
- One
"""