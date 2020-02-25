def phone_directory():
    print(dict1)
dict1={}
for i in range(12):
    dict1[input("Enter name to save : ")] = int(input("Enter num you want to add: "))
phone_directory()
def phone2():
    del dict1["Saleem"]
    print(dict1)
phone2()




family={"Father's Name" : "M.Tariq",
        "Mother's Name" : "Fouzia Tariq",
        "Siblings" : ["Sajjad Tariq","Ayyan Tariq","Salih Tariq"]}
print(family)
grandfamily={"Maternal":{"Grandfather" : "M.Farooq","Grand Mother" : "Qamar_un_Nisa","Uncle" : "M,Arif","Aunts" : ["Rehana","Abida"]},
             "Paternal":{"Grandfather" : "Abdul Majeed", "Grand Mother" : "Shahida","Uncle" : ["Rafiq","Ilyas"],"Aunt" : []}}
family.update(grandfamily)
print(family)


def hexaAscii():
    y="Software".lower()
    z={}
    for i in y:
        z[i]=hex(ord(i))
    return z
print(hexaAscii())



a={"DishesOfMyChoice":["pizza","biryani","karahi","burger","BBQ","Qourma","tikka","nihari","pasta"]}
b={"DishesCooked":["biryani","nihari","Qourma","sandwich","chinese rice","pilao","karahi","BBQ","tikka"]}
for i in a.values():
    x=set(i)
for j in b.values():
    y=set(j)
z=x.intersection(y)
u=list(z)
l=len(z)
print("You will get",l,"Dishes:")
print(u)






parentslist=['Aslam','Akram','Saad','Salih','Anum','Sajjad','Rehana','Shahida','Asif']
mylist=['Aslam','Salih','Raheel','Ubaid','Ayyan','Rehana','Arif','Rafiq','Ilyas']
a1=set(parentslist)
b1=set(mylist)
c=a1.intersection(b1)
d=a1.difference(c)
e=b1.difference(c)
f=d.union(e)
g=f.union(c)
y=list(g)
c1=len(c)
d1=len(d)
e1=len(e)
sum=c1+d1+e1
print("The Guests I invited are:\n",mylist)
print("The Guests my parents invited are:\n",parentslist)
print("The guests invited are:","\n",y)
print("The total guests invited are: ",sum)

