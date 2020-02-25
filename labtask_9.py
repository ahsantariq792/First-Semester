bestfriend=set({})
for i in range(5):
    a=input("Enter Your best friend name:")
    bestfriend.add(a)
print(bestfriend)





friendsleft=set({})
friendsinUIT=set({})
for i in range(8):
    z=input("Enter friends who are studying in UIT: ")
    friendsinUIT.add(z)
for i in range(2):
    x=input("Enter friends who left UIT: ")
    friendsleft.add(x)
    y=friendsinUIT-friendsleft
print("friends who were studying in UIT are\n",friendsinUIT)
print("friends who left UIT are\n",friendsleft)
print("friends who are studying in UIT now are\n",y)





s1={'item1','item2','item3','item4'}
d1={}
l1=[]
for i in range(len(s1)):
    a=s1.pop()
    print("For",a)
    d1[a]=int(input("Enter price: "))
print(d1)
for i in d1.values():
    l1.append(i)
print(l1)
print("Total Amount of items sold are",sum(l1))
print("The maximum price is {}".format(max(l1)))
print("The minimum price is {}".format(min(l1)))






A=21
AUB=40
AnB=10
B=(AUB)-(AnB)-(A)
print("Students playing both hockey and cricket are",AnB)
print("Students playing hockey only are",A)
print("Students playing cricket only are",B)





x=set({})
for i in range(5):
    a=input("Enter your best dishes:")
    x.add(a)
print(x)
for i in range(5):
    x.pop()
    print(x)







total=set(range(110))
e=set(range(25))
s=set(range(10))
f=set(range(11))
e_s=set(range(20))
e_f=set(range(17))
f_s=set(range(9))
all=set(range(13))
none=len(total)-(len(e)+len(s)+len(f)+len(e_s)+len(f_s)+len(e_f)+len(all))
print("students speaking only english and french are",len(e_s))
print("students speaking none of english spanish and french are",none)
print("students speaking only french are",len(f))
print("students speaking one of three are",len(e)+len(s)+len(f))
print("students speaking one of three are",len(e_s)+len(f_s)+len(e_f))




dog=set(range(1,84))
cat=set(range(47,148))
fish=set(range(72,78))|(set(range(138,154)))|set(range(1,9))
other=set(range(155,189))
onlydog=dog-(cat|fish)
onlycat=cat-(dog|fish)
onlyfish=fish-(dog|cat)
total=dog|fish|cat|other
onlycatndog=(cat&dog)-fish
onlycatnfish=(cat&fish)-dog
onlydognfish=(dog&fish)-cat
allthree=cat&fish&dog
print("{:^40}".format("GIVEN DATA"))
data={"dog product":len(dog),"cat product":len(cat),"fish product":len(fish),
      "a cat and a dog product":len(onlycatndog),
      "a dog and a fish product":len(onlydognfish),
      "a cat and a fish product":len(onlycatnfish),
      "a cat, a fish and a dog product":len(allthree),
      "a product other than a cat, dog and a fish product":len(other)}
for i,j in data.items():
    print("People who purchased",i,"=",j)
print("{:^40}".format("ANSWERS"))
print("People who purshased only dog product:",len(onlydog))
print("People who purshased only cat product:",len(onlycat))
print("People who purshased a dog or a fish product:",len(onlyfish|onlydog))
print("Total purchases=",len(total))

