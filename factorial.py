
def Factorial(n,fact=1):
    if n>0:
        fact=n*Factorial(n-1)
        return fact
    else:
        return fact
print(Factorial(7))
