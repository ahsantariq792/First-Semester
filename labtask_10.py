import os
def abc(filename):
    f=open(filename,"r+")
    a=f.read()
    b=a.split()
    c=""
    for i in b:
        if(len(i)==4):
            c+="XXXX"
        else:
            c+=i
        c+=""
    z=open(filename,"w")
    d=z.write(c)
filename=input("Enter filename that you want to open")
abc(filename)



def duplicate(filename):
    with open(filename, 'r') as f:
        words = set()
        for line in f.readlines():
            lineWords = line.split()
            for word in lineWords:
                if word in words:
                    return True

                words.add(word)
    return False

w= duplicate('D:\\ahsan.txt')
print(w)



import os
def stats(filename):
    a = open(filename)
    print("line count:",len(a.readlines()))
    a.close()
    a=open(filename)
    print("character count",len(a.read()))
    a.close()
    a=open(filename)
    print("count",len(a.read().split()))
    a.close()
filename=input("Enter filename that you want to open")
stats(filename)


import os
l=list()
def distributuion(filename):
    filename=open(filename)
    s=filename.read().split()
    print("The students who get A are:",(s.count("A")))
    print("The students who get B are:",(s.count("B")))
    print("The students who get B+ are:",(s.count("B+")))
    print("The students who get B- are:",(s.count("B-")))
    print("The students who get C are:",(s.count("C")))
    print("The students who get C- are:",(s.count("C-")))
    print("The students who get F are:",(s.count("F")))
filename=input("Enter filename that you want to open")
distributuion(filename)



