import os

with open('7r.txt','r') as file:
    file=file.read()

file=file.split('\n')
f=[]
for line in file:
    line=line.split()
    f.append(line)
file=f

cwd=''
dir_dict={'/':0}
for command in file:
    if command[0] == '$':
            if command[1] == 'ls':
                pass
            else:
                if command[2] == '..':
                    cwd = cwd[:cwd.rindex('/')]
                elif command[2] == '/':
                    cwd = '/'
                else:
                    cwd= cwd+ '/'+command[2]
                    dir_dict[cwd] = 0
    
    else:
        if command[0] != 'dir':
            temppath=cwd
            while temppath != '': #this is the key to avoidi
                dir_dict[temppath] +=  int(command[0])
                temppath = temppath[:temppath.rindex('/')]


sum=0
for k,v in dir_dict.items():
    if v <= 100000:
        sum +=v

sum=0
for k,v in dir_dict.items():
    root_dir_size = v
    break

# print (f"{root_dir_size:,d}")
total_disk_space = 70000000
program_space = 30000000
empty_space = total_disk_space - root_dir_size
needed_space = program_space - empty_space

ans=[]
for k,v in dir_dict.items():
    if v > needed_space:
        ans.append(v)

# ans=ans.sort()
print(ans)
print(min(ans))

#first take sum of ALL keys
#then iterate, while sum -value if cwd < threshold
#finding the outer leaves is non-trivial, just go naive

# Task 2: Get the smallest directory that can be deleted, in order to have at least 30000000 free space, with 70000000
#         being the total disk space available
#         elif command[1] == 'ls':
#             continue#)
#             for command in file:
#                 if command[0] == '$':
#                     break
#                 if command[0] == 'dir':
#                     continue
#                 else: #command is a filesize number
#                     dir_dict[cwd] += int(command[0])

