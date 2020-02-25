from math import*
def angle(x,y):
    for i in range(x,y+1):
        a=sin(i)
        b=cos(i)
        c=tan(i)
        print(i,"\t\t\t",round(a,2),"\t\t\t",round(b,2),"\t\t\t",round(c,2))
x=int(input("enter starting range:"))
y=int(input("enter ending range:"))
print()
print("TABLE OF TRIGNOMETRIC FUNCTIONS")
print("Angle(ϴ)","\t","sin(ϴ)","\t\t","cos(ϴ)","\t\t","tan(ϴ)")
result=angle(x,y)
