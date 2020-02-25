from math import*
def area(radius,height):
    a=(2*pi*r*h)+(2*pi*r**2)
    return a
def volume(radius,height):
    v=pi*(r**2)*h
    return v
r=float(input("enter radius of cylinder"))
h=float(input("enter height of cylinder"))
print("area of sphere is",area(r,h))
print("Volume of sphere is",volume(r,h))


















from math import*
def area(l,w):
    a=l*w
    return a
def volume (l,w,h):
    v=l*w*h
    return v
l=float(input("enter length of rectangle"))
w=float(input("enter width of rectangle"))
h=float(input("enter height of rectangle"))
print("Area of rectangle is",area(l,w))
print("Volume of rectangle is",volume(l,w,h))










L1=[37,2,6,4,90,45,67,21]
print("The Given numbers are =",L1)
L1.sort()
print("Numbers arranged in ascending order are =",L1)






def reversed(string):
    n=(string[::-1])
    return string
string=input("enter a string")
print(string.casefold())
if (string==reversed(string)):
    print("Yes,the string is palindrome")
else:
    print("Sorry,the string is not palindrome")













def reversed(n):
    n=(name[::-1])
    return n
name=input("enter your name")
print()
print("your original name is",name)
print("the reversed name is",reversed(name))
