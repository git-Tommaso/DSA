counter = 0

def fibonacci(n):
   fib_list = [0, 1]
   global counter
   for index in range(2, n + 1):
      counter += 1
      next_fib = fib_list[index - 1] + fib_list[index - 2]
      fib_list.append(next_fib)
   return fib_list[n]

n = 10

print("\nFibonacci of ",n, " = ", fibonacci(n))
print("\nCounter: ", counter)

n = 20

print("\nFibonacci of ",n, " = ", fibonacci(n))
print("\nCounter: ", counter)

n = 30

print("\nFibonacci of ",n, " = ", fibonacci(n))
print("\nCounter: ", counter)