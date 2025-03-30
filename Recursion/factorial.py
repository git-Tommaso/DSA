def factorial(n):
   if n == 1:
      return 1
   else:
      return n * factorial(n-1)
   
print(factorial(4))


"""
4! = 4 * 3 * 2 * 1 = 24

4!
4 * 3!
    3 * 2!
        2 * 1!
            1
"""