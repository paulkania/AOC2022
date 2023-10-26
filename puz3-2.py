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

print(file)

sum=0
shared_item=[]

while file:
    sack1=file[0]
    sack2=file[1]
    sack3=file[2]
    for item in sack1:
        if item in sack2:
            if item in sack3:
                if item.islower():
                    sum+=ord(item)-96
                    shared_item.append(item)
                else:
                    sum+=ord(item)-96+58
                    shared_item.append(item)
                file=file[3:]
                break


                



end = time.time()
print(sum)  
print(shared_item)  
print(len(shared_item))  
print(end-start)  