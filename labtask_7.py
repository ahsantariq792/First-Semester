l=[(2, 3), (4, 7), (8, 11), (3, 6), (10, 2)]
for i in range(len(l)):
    x=min(l[i])
    y=max(l[i])
    print("The min value is",x)
    print("The max value is",y)




from math import*
for i in range(0,4):
    x,y=eval(input("Enter dart  co_ordinate: "))
    z=(sqrt(x**2+y**2))
    if z<10:
        print("True")
    else:
        print("False")





t=(())
l=list(t)
for i in range(4):
    x=input("Enter Province: ")
    l.append(x)
t=tuple(l)
print(t)




L1=[37,2,6,4,90,45,67,21]
print(L1)
n=len(L1)
for i in range(0,n):
    for j in range(i+1,n):
        temp = L1[i]
        if (L1[i]>L1[j]):
            temp=L1[j]
            L1[j]=L1[i]
            L1[i]=temp
print("The Numbers in Ascending order are arranged as :")
print (L1)