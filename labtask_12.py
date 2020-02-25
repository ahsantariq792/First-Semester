from random import*
cities=['Karachi','Peshawar','Lahore','Quetta','Islamabad','Multan','Hyderabad','Faisalabad','Sialkot']
shuffle(cities)
print(cities)



from random import*
Students=['Sajjad','Asad','Areeb','Osama','Maaz','Ali','Ahmas','Anas']
l1=[]
for i in range(len(Students)):
    b=Students.pop()
    l1.append(b)
print(l1)
c=sample(l1,2)
print("The students selected for scholarship are",c)



from random import*
Dice_1=[1,2,3,4,5,6]
Dice_2=[1,2,3,4,5,6]
print("From Dice 1 you get",choice(Dice_1))
print("From Dice 2 you get",choice(Dice_2))

