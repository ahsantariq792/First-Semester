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



from math import*
i=0
j=0
for i in range(0,7):
    for j in range (0,i):
        print("*",end="")
    print()
    j=0



from math import*
i=0
j=0
for i in range(0,7):
    for j in range (0,8):
        print("*",end="")
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



j=9
for i in range(1,10,2):
    print(" "*j+i*"*")
    j=j-1




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



