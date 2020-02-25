import cmath
def Quad(a,b,c):
    d=(b**2)-(4*a*c)
    if (a <= 0):
        print("no solution")
    else:
        s1=(-b-(cmath.sqrt(d)))/2*a
        s2=(-b+(cmath.sqrt(d)))/2*a
    return s1,s2
a=float(input("enter value of a"))
b=float(input("enter value of b"))
c=float(input("enter value of c"))
s1,s2= Quad(a,b,c)
print("the solution are {0} and {1}".format(s1,s2))




def reversed(string):
    n=(string[::-1])
    return string
string=input("enter a string")
print(string.casefold())
if (string==reversed(string)):
    print("Yes,the string is palindrome")
else:
    print("Sorry,the string is not palindrome")






for i in range (11,17):
    for j in range (1,6):
        print(i,end="\t")
    print()






from math import*
maxmarks=100
name=input("enter your name")
fname=input("enter your father name")
rno=int(input("enter your roll number"))
sub1=input("enter first subject name")
sub2=input("enter second subject name")
sub3=input("enter third subject name")
sub4=input("enter fourth subject name")
sub5=input("enter fifth subject name")
marks1=int(input("enter marks obtained in first subject"))
marks2=int(input("enter marks obtained in second subject"))
marks3=int(input("enter marks obtained in third subject"))
marks4=int(input("enter marks obtained in fourth subject"))
marks5=int(input("enter marks obtained in fifth subject"))
totalmarks= marks1+marks2+marks3+marks4+marks5
percentage=totalmarks/5
if percentage>=80 and percentage<=99 :
    Grade = "A+"
elif percentage>=70 and percentage<= 79:
    Grade = "A"
elif percentage>=60 and percentage<= 69:
    Grade = "B"
elif percentage >= 50 and percentage <= 59:
    Grade = "C"
elif percentage >= 40 and percentage <= 49:
    Grade = "D"
else :
    print("Grade = F")
print("\n")
print("Student Name :",name)
print("Father Name :",fname,"\t\t\t\tRoll Number :",rno)
print("Percentage :",percentage,"%","\t\t\t\t\t\tGrade :",Grade)
print()
print("\t","Subjects","\t\t","Max. Marks","\t\t","Marks Obtained")
print("\t\t",sub1,"\t\t\t",maxmarks,"\t\t\t\t",marks1)
print("\t\t",sub2,"\t\t\t",maxmarks,"\t\t\t\t",marks2)
print("\t\t",sub3,"\t\t\t",maxmarks,"\t\t\t\t",marks3)
print("\t\t",sub4,"\t\t\t",maxmarks,"\t\t\t\t",marks4)
print("\t\t",sub5,"\t\t\t",maxmarks,"\t\t\t\t",marks5)
print()
print("\t\t\t\t\t\t\t\t\t\t\t","Total Marks Obtained =" ,totalmarks)







from math import*
a=int(input("Enter number of values for table:"))
b=int(input("Enter starting Range:"))
c=int(input("Enter Ending Range:"))
for i in range(1,a+1):
    for j in range(b,c+1):
        print(i*j,end=" ")
    print("\t")







a=int(input("Enter value of matrix A 1*1 :"))
b=int(input("Enter value of matrix A 1*2 :"))
c=int(input("Enter value of matrix A 2*1 :"))
d=int(input("Enter value of matrix A 2*2 :"))
e=int(input("Enter value of matrix B 1*1 :"))
f=int(input("Enter value of matrix B 1*2 :"))
g=int(input("Enter value of matrix B 2*1 :"))
h=int(input("Enter value of matrix B 2*2 :"))
A=[[a,b],[c,d]]
B=[[e,f],[g,h]]
C=[[0,0],[0,0]]
print("Matrix A is",A)
print("Matrix B is",B)

for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j]=A[i][j]+B[i][j]
    print("The Result of addition is:",C[i][j],end="\t")








a=int(input("Enter value of matrix A 1*1 :"))
b=int(input("Enter value of matrix A 1*2 :"))
c=int(input("Enter value of matrix A 2*1 :"))
d=int(input("Enter value of matrix A 2*2 :"))
e=int(input("Enter value of matrix B 1*1 :"))
f=int(input("Enter value of matrix B 1*2 :"))
g=int(input("Enter value of matrix B 2*1 :"))
h=int(input("Enter value of matrix B 2*2 :"))
A=[[a,b],[c,d]]
B=[[e,f],[g,h]]
C=[[0,0],[0,0]]
print("Matrix A is",A)
print("Matrix B is",B)
print("The solution of AxB is:")
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j]=A[i][i-1]*B[i-1][j]+A[i][i]*B[i][j]
for i in C:
    print(i)

