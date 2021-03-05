import random
openedfile=open("input.txt")
num=list()
new=[]
for line in openedfile:
    number=line.rstrip().split()
    for interger in number:
        if interger in num:
            continue
        else :
            num.append(interger)
num.sort()
for interger in num:
    new.append(int(interger))
newlst=[]
for a in num:
    for b in new:
        a=random.choice(new)
        b=random.choice(new)
        addition=a+b
        while  addition == 3333:
            product=a*b
            #print(product,"is the product of",a,"and",b)
            newlst.append(product)
            break
print(newlst)
