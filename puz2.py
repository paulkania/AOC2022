import os
import time

start = time.time()

with open('2r.txt','r') as file:
    file=file.read()

file=file.split('\n')
def part1():
    score=0
    for throw in file:
        if throw[0] == 'A' and throw [2] == 'X':
            score += 1 + 3
            continue
        if throw[0] == 'A' and throw [2] == 'Y':
            score += 2 + 6
            continue
        if throw[0] == 'A' and throw [2] == 'Z':
            score += 3 + 0
            continue

        if throw[0] == 'B' and throw [2] == 'X':
            score += 1 + 0
            continue
        if throw[0] == 'B' and throw [2] == 'Y':
            score += 2 + 3
            continue
        if throw[0] == 'B' and throw [2] == 'Z':
            score += 3 + 6
            continue

        if throw[0] == 'C' and throw [2] == 'X':
            score += 1 + 6
            continue
        if throw[0] == 'C' and throw [2] == 'Y':
            score += 2 + 0
            continue
        if throw[0] == 'C' and throw [2] == 'Z':
            score += 3 + 3
            continue
    return score


def part2():
    score=0
    for throw in file:
        if throw[0] == 'A' and throw [2] == 'X': #A rock
            score += 3 + 0
            continue
        if throw[0] == 'A' and throw [2] == 'Y':
            score += 1 + 3
            continue
        if throw[0] == 'A' and throw [2] == 'Z':
            score += 2 + 6
            continue

        if throw[0] == 'B' and throw [2] == 'X': # B paper
            score += 1 + 0
            continue
        if throw[0] == 'B' and throw [2] == 'Y':
            score += 2 + 3
            continue
        if throw[0] == 'B' and throw [2] == 'Z':
            score += 3 + 6
            continue

        if throw[0] == 'C' and throw [2] == 'X': # C opponents scissors
            score += 2 + 0
            continue
        if throw[0] == 'C' and throw [2] == 'Y':
            score += 3 + 3
            continue
        if throw[0] == 'C' and throw [2] == 'Z':
            score += 1 + 6
            continue
    return score

end = time.time()
print(part2(), 'aids')
print(end-start)