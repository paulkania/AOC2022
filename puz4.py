import os
import time

t1=time.time()
t2=time.time()


with open('4r.txt','r') as file:
    file=file.readlines()

f2=[]
for item in file:
    item=item.replace('\n','')
    f2.append(item)

f3=[]
for i in f2:
    i=i.split(',')
    f3.append(i)


f4=[]
for masterlist in f3:
    i=masterlist[0].split('-')
    j=masterlist[1].split('-')
    f4.append(i)
    f4.append(j)

f5=f4 #used for part 2
# print(f4)


def part1():
    sum=0
    global f4
    while(f4):
        elf1 = f4[0]
        elf2 =f4[1]
        f4=f4[2:]
        if (int(elf1[0])) <= (int(elf2[0])) and (int(elf1[1])) >= (int(elf2[1])):
            sum+=1
            continue
        elif (int(elf1[0])) >= (int(elf2[0])) and (int(elf1[1])) <= (int(elf2[1])):
            sum+=1
            continue
    return (sum)
    
def part2():
    sum2=0
    global f5
    while (f5):
        elf1 = f5[0]
        elf2 =f5[1]
        x= elf1[0]
        y= elf1[1]
        z = elf2[0]
        k = elf2[1]
        f5=f5[2:]
        if (y <=k and y >= z):
            sum2+=1
            continue
        elif (x>= z and y <=z ):
            sum2+=1
            continue
        elif (z>= x and z <=y ):
            sum2+=1
            continue
        elif (k >= x and k <= y ):
            sum2+=1
            continue
    return sum2


print(part2())