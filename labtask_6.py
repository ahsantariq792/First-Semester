L=[2, 1, 3, 5, 4, 3, 8]
del(L[2])
print(L)
L=[2, 1, 3, 5, 4, 3, 8]
L.remove(4)
print(L)
L=[2, 1, 3, 5, 4, 3, 8]
L.sort()
print(L)
L=[2, 1, 3, 5, 4, 3, 8]
L.insert(2,9)
print(L)
L=[2, 1, 3, 5, 4, 3, 8]
L.pop()
print(L)
L=[2, 1, 3, 5, 4, 3, 8]
L1=[6,7]
L.extend(L1)
print(L)







a=6
b=7
print(a,b)
c=(a+b)/2
print("avg of a and b is",c)
inventory=["paper","staples","pencils"]
print(inventory)
first=["John"]
middle=["Fitzgerald"]
last=["Kennedy"]
fullname=(first+middle+last)
print(fullname)









#for list:
monthsL=["Jan","Feb","Mar","May"]
print(monthsL)
monthsL.insert(3,"Apr")
print("(a)",monthsL)
monthsL.append("Jun")
print("(b)",monthsL)
monthsL.pop()
print("(c)",monthsL)
monthsL.remove("Feb")
print("(d)",monthsL)
monthsL.reverse()
print("(e)",monthsL)

#for tuple:
monthsT=("Jan","Feb","Mar","May")
print(monthsT)
monthsT.insert(3,"Apr")
print("(a)",monthsT)
monthsT.append("Jun")
print("(b)",monthsT)
monthsT.pop()
print("(c)",monthsT)
monthsT.remove("Feb")
print("(d)",monthsT)
monthsT.reverse()
print("(e)",monthsT)




L1=[42,23,34,64,58,16,8]
a=len(L1)
b=int(a/2)
print("(a)The index of middle element is",b)
print("(b)The middle element is",L1[b])
L1.sort(reverse=True)
print("(c)list in descending order is:",L1)
L1=[42,23,34,64,58,16,8]
L1.append(L1[0])
L1.remove(L1[0])
print("(d)",L1)









from math import*
print("Using formula: height=lenght*sin(angle)")
l1=16
l2=20
l3=l4=24
angle1=75
angle2=0
angle3=45
angle4=80
rad1=angle1*(pi/180)
rad2=angle2*(pi/180)
rad3=angle3*(pi/180)
rad4=angle4*(pi/180)
h1=l1*sin(rad1)
h2=l2*sin(rad2)
h3=l3*sin(rad3)
h4=l4*sin(rad4)
print("(a)The height reached by ladder is",round(h1,2),"feet")
print("(b)The height reached by ladder is",round(h2,2),"feet")
print("(c)The height reached by ladder is",round(h3,2),"feet")
print("(d)The height reached by ladder is",round(h4,2),"feet")

