def Factorial(n):
    return 1 if (n == 1 or n == 0) else n * Factorial(n-1);


p = 1
for i in range(5):
  p = p + "Factorial(n)/n"