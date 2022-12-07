def Factorial(n):
    return 1 if (n == 1 or n == 0) else n * Factorial(n-1);


num = 7;
print("Factorial of",num,"is", Factorial(num))    