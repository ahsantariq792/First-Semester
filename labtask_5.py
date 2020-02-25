import random
i=0
while (i<100):
    i = i+1
    if(i%2!=0):
        print(i)




from math import*
i=0
j=0
while (i<=7):
    if i<=3:
        while(j<=13):
            print("*",end="")
            j=j+1
    elif i>3:
        print(" "*17,end="")
        while (j<=13):
            print("*", end="")
            j=j+1
    i=i+1
    j=0
    print()









from math import*
i=0
j=0
while (i<=7):
    i=i+1
    while(j<i):
        print("*",end="")
        j=j+1
    print()
    j=0





from math import*
i=0
j=0
while (i<=7):
    i=i+1
    while (j<=8-i):
        print("*",end="")
        j=j+1
    print()
    j=0




n=0
def factorial(x):
    fact=1
    for i in range (1,x+1):
        fact=fact*i
    return fact
while n>=0 and n<=10:
    print(n,"!=",factorial(n))
    n=n+1
