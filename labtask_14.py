from sys import*
L1=[4,6,8,10,12,18,20]
L2=[2,0,4,5,4,3]
for i in range(len(L1)):
    try:
        a=L1[i]//L2[i]
        print(L1[i],"divided by",L2[i],"is",a)
    except IndexError as x:
        print("list Out of range")
    except ZeroDivisionError as y:
        print("Division by zero is not possible")




from sys import*
try:
    a=input("Enter your Name")
    print(a)
except EOFError as e:
    print("Error,Enter Your Name")



from sys import*
try:
    # This file contains indentation error
    import scratch_19.py
except IndentationError:
    print("Indentation Error Occurred")



from sys import*
try:
    a=open("D:/hello.py")
    print(a.read())
except IOError :
    print("IO Error is Occurred")

