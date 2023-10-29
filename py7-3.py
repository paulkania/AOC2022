import os

with open('7f.txt','r') as file:
    file=file.read()

file=file.split('\n')
f=[]
for line in file:
    line=line.split()
    f.append(line)
file=f

Directory=()
Directory.children = []
Directory.cwd = ''

dir_list=[]
while file:
    command = file[0]
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] != '..':
                cwd = cwd + '.' + command[2]
                dir_dict[cwd] = 0
                
            elif command[2] == '..':
                cnt=0
                for element in cwd[::-1]:
                    cnt+=1
                    if element == '.':
                        cwd = cwd[0:-cnt]
        elif command[1] == 'ls':
            while file[1][0] != '$':
                file=file[1:]       
                if command[0] == '$':
                    break
                if command[0] == 'dir':
                    continue
                else: #command is a filesize number
                    dir_dict[cwd] += int(command[0])
                    file=file[cont:]
