import os

print(os.getcwd())

with open('1r.txt','r') as file:
    file = file.read()


file=file.split('\n')
# print(file)

calorie_counter=0
highscore = []

for snack in file:
    if not snack:
        highscore.append(calorie_counter)
        calorie_counter = 0
        continue
    calorie_counter += int(snack)
        

highscore.sort()
ans = highscore[-1]+highscore[-2]+highscore[-3]

print(ans)
