from math import*
def factorial(n):
    if (n==1):
        return 1
    else :
        return n*fact(n-1)
fact=1
i=1
while (i<=10):
    fact=fact*i
    i=i+1
n=10
check=factorial(i)
print("the factorial of is",check)









from math import*
def fact1(x):
    fact=1
    return fact
i=0
fact=1
fact=i*fact(i-1)
while (i<=10):
    i= i+1
    print(i,"!","\t=",fact1(i))
