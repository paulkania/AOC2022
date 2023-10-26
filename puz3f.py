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
import string

start = time.time()

with open('3r.txt','r') as file:
    file=file.read()

file=file.split('\n')


sum=0
c=0

for rucksack in file:
    halfpoint = int(len(rucksack)/2)
    compartment1 = rucksack[:halfpoint]
    compartment2 = rucksack[halfpoint:]
    for item in compartment1:
        if item in compartment2:
            c+=1
            if item.islower():
                sum+=ord(item)-96
            else:
                sum+=ord(item)-96+58
            break



print(sum)
end = time.time()
print(end-start)  
#301   
