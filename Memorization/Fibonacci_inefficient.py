counter = 0

def fibonacci(n):
   global counter
   counter += 1
   if n == 0 or n== 1:
      return n
   return fibonacci(n -1) + fibonacci(n - 2) 

n = 10

print("\nFibonacci of ",n, " = ", fibonacci(n))
print("\nCounter: ", counter)

n = 20

print("\nFibonacci of ",n, " = ", fibonacci(n))
print("\nCounter: ", counter)

n = 30

print("\nFibonacci of ",n, " = ", fibonacci(n))
print("\nCounter: ", counter)