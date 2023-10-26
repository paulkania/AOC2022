# x = open("3r.txt", "r").read().splitlines()

# t = 0
# c=0
# from string import ascii_uppercase, ascii_lowercase

# for i in x:
#     a,b=i[:len(i)//2], i[len(i)//2:]

#     for r in a:
#         if r in b:
#             if r.islower():t+=ascii_lowercase.index(r)+1
#             else:t+=ascii_uppercase.index(r)+27
#             c+=1
#             break


# print(t,c)


import os
import time

start = time.time()

with open('3r.txt','r') as file:
    file=file.read()

file=file.split('\n')


shared_item=[]
itemfound = False
deadlines=[]
sum=0


for rucksack in file:
    halfpoint = int(len(rucksack)/2)
    compartment1 = rucksack[:halfpoint]
    compartment1 += '1' # hacky workaround so i wasnt getting a missed match
    compartment2 = rucksack[halfpoint:]
    compartment2 += '3'
    # compartment2[-1]='4'
    for item in compartment1:
        if itemfound:
            itemfound = False
            break
        for i in compartment2:
            if item == i:
                shared_item.append(item)
                itemfound = True
                break
                


for item in shared_item:
    if item.islower():
        sum+=ord(item)-96
    elif item.isupper():
        sum+=ord(item)-96+58

print(len(shared_item))

print(sum)
end = time.time()
print(end-start)  
#301   
