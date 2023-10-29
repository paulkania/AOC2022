import os
import time

t1= time.time()
with open('7r.txt','r') as file:
    file=file.read()

file=file.split('\n')

f=[]
for line in file:
    line=line.split()
    f.append(line)

directory_list=[]
class Directory():
    cwd = ''
    children = []
    score =0


cwd = ''
pwd= ''
pwds=[]
for command in f:
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                cwd = cwd[:-len(pwd)]
                f=f[1:]
                continue
            else:
                cwd = cwd + '/'+ command[2]
                pwd = command[2]
                f=f[1:]
                continue
        elif command[1] == 'ls':
            pass

print(pwds)
#non nested
nested_dirs = []
dir_dict={}
for directory in directory_list:
    while directory.children:
        if directory.children[0] == 'dir':
            nested_dirs.append(directory.cwd + directory.children[1])
            directory.children = directory.children[2:]
        else:
            directory.score += int(directory.children[0])
            directory.children = directory.children[2:]
    dir_dict[directory.cwd] = directory.score


#nested
for directory in directory_list:
    if not nested_dirs:
        break
    nested_dir = nested_dirs[0]
    nested_dirs = nested_dirs[1:]
    for d2 in directory_list:
        if directory.cwd == d2.cwd[:-69]: #the problem is here. goodnight xo
            directory.score += d2.score

sum=0
for d in directory_list:
    if d.score <= 100000:
        sum+=d.score
t2=time.time()
print(sum) #correct == 1325919
print(t2-t1)
print(pwds)


# for k,v in dir_dict.items():
#     print(k,v)