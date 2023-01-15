from random import randint
l=[]
L=[]
n=0
for i in range(10000):
    for i in range(100):
        a=randint(0,1)
        l.append(a)
    s=0        
    for i in range(1,len(l)):
        if l[i]==l[i-1]:
            s+=1
        if l[i]!=l[i-1]:
            s=0
        if s==6:
            n+=1
            s=0
    l=[]
                
print(n/100)