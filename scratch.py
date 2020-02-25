age=int(input("enter your age"))
if (age<65):
    ryears = 65 - age
    print("you have",ryears,"till retirement")
else:
    print("invalid age")




from math import*
r=float(input("enter radius of circle"))
area= pi*r**2
circumference=2*pi*r
print("Using radius",r,"\n","the area of circle is",area,"\n""and circumference of circle is",circumference)




tno=int(input("enter table number"))
rang=int(input("enter your range"))
for i in range (1,rang+1):
    c=tno*i
    print(tno,"\t","*",i,"=","\t",c)





salary=int(input("enter your salary"))
grade=int(input("enter your grade"))
if (grade>=1) or (grade<=16):
    increment=0.2*salary
    newsalary=increment+salary
    print("the increment is",increment,"\n", "the new salary is", newsalary)
elif (grade>=17) or (grade<=19):
    increment=0.1*salary
    newsalary=increment+salary
    print("the increment is",increment,"\n","the new salary is",newsalary)
elif (grade>=20) or (grade<=22):
    increment=0.05*salary
    newsalary=increment+salary
    print("the increment is",increment,"\n","the new salary is", newsalary)
else:
    print("invalid input")



















