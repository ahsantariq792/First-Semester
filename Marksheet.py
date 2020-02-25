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
print("\t\t","Subjects","\t\t","Max. Marks","\t\t","Marks Obtained")
print("\t\t",sub1,"\t\t\t",maxmarks,"\t\t\t\t",marks1)
print("\t\t",sub2,"\t\t\t",maxmarks,"\t\t\t\t",marks2)
print("\t\t",sub3,"\t\t\t",maxmarks,"\t\t\t\t",marks3)
print("\t\t",sub4,"\t\t\t",maxmarks,"\t\t\t\t",marks4)
print("\t\t",sub5,"\t\t\t",maxmarks,"\t\t\t\t",marks5)
print()
print("\t\t\t\t\t\t\t\t\t\t\t","Total Marks Obtained =" ,totalmarks)
