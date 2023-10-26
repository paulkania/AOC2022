import os
import time
t1=time.time()

with open('5r.txt','r') as file:
    file=file.read()
# crates = ['placeholder','NZ', 'DCM', 'P']
crates = ['placeholder','NHSJFWTD', 'GBNTQPRH', 'VQL', 'QRWSBN','BMVTFDN','RTHVBDM','JQBD','QHZRVJND','SMHNB']


file = file.split()
def part1():
    global file
    crates = ['placeholder','NHSJFWTD', 'GBNTQPRH', 'VQL', 'QRWSBN','BMVTFDN','RTHVBDM','JQBD','QHZRVJND','SMHNB']
    while file:
        count = int(file[1]) 
        column_origin = int(file[3])
        column_deposit = int(file[5])
        while count > 0:
            count -= 1
            crate = crates[column_origin][0]
            crates[column_deposit] = crate + crates[column_deposit]
            crates[column_origin] = crates[column_origin][1:]
        file=file[6:]


    crates=crates[1:]
    ans=''
    for crate in crates:
        ans+= crate[0]
    return(ans)

def part2():
    global file, crates
    while file:
        count = int(file[1]) 
        column_origin = int(file[3])
        column_deposit = int(file[5])
        crate = crates[column_origin][0:count]
        crates[column_deposit] = crate + crates[column_deposit]
        crates[column_origin] = crates[column_origin][count:]
        file=file[6:]


    crates=crates[1:]
    ans=''
    for crate in crates:
        ans+= crate[0]
    return(ans)
    t2=time.time()
    print(t2-t1)

print(part2())

### a visualizer for this puzzle would be very nice.
