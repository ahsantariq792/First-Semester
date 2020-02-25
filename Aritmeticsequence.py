def sequence(n):
    an=a1+(n-1)*d
    return an
a1=int(input("Enter first Term :"))
d=int(input("Enter Common Difference :"))
n=int(input("Enter number of terms :"))
print("The nth Term of the sequence is :",sequence(n))
x=input("Do you want to calculate more Terms ?(yes/no)")
while(x=="yes"):
    n=int(input("Enter number of terms :"))
    print("The nth Term of the sequence is :",sequence(n))
    x = input("Do you want to calculate more Terms ?(yes/no)")
else:
    print ("End")


