from math import*
def eq1(Vi,a,t):
    Vf=Vi+a*t
    return Vf
Vi=float(input("Enter Initial Velocity in m/s"))
a=float(input("Enter Acceleration in m/s²"))
t=float(input("Enter time in s"))
result1=eq1(Vi,a,t)
print("Using first eq of motion : Vf=Vi+a*t")
print("The Final velocity is:",result1,"m/s")
print()
def eq2(Vi,t,a):
    S=(Vi*t)+(1/2)*a*t**2
    return S
Vi=float(input("Enter Initial Velocity in m/s"))
a=float(input("Enter Acceleration in m/s²"))
t=float(input("Enter Time taken in s"))
result2=eq2(Vi,t,a)
print("Using Second eq of motion :  S=(Vi*t)+(1/2)*a*t**2 ")
print("The Distance covered is:",result2,"m")
print()
def eq3(Vf,Vi,s):
    a=((Vf**2)-(Vi**2))/2*s
    return a
Vi=float(input("Enter Initial Velocity in m/s"))
Vf=float(input("Enter Final Velocity in m/s"))
s=float(input("Enter Distance covered in m"))
result3=eq3(Vf,Vi,s)
print("Using Third eq of motion : 2*a*s=(Vf**2)-(Vi**2) ")
print("The Acceleration is:",result3,"m/s²")

