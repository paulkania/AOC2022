import time as t
t1=t.time()
with open('11r.txt','r') as input:
    input = input.read().splitlines()

# print(input[0][7:].removesuffix(':')) #monkey ID
# print(input[1][18:]) #starting Items
# print(input[2][25:]) # Operand
# print(input[3][21:]) # test_divisor
# print(input[4][29:]) # t_true
# print(input[5][30:]) # t_false

class Monkey:
    Id = int
    Items = []
    Op = ''
    Operand = int
    Test_divisor = int
    Tcase = int
    F_case = int

monkeys=[]
while input:
    monkey = Monkey()
    monkey.Inspection_count = 0
    monkey.Id = int(input[0][7:].removesuffix(':')) #monkey ID
    monkey.Items = input[1][18:].split(',') #starting Items
    monkey.Op = input[2][23:24]
    monkey.Operand =input[2][25:]# Operand can be old
    monkey.Test_divisor =int(input[3][21:]) # test_divisor
    monkey.Tcase =int(input[4][29:]) # t_true
    monkey.F_case =int(input[5][30:]) # t_false 
    monkeys.append(monkey) 
    input=input[7:]

divisor= 1
for monkey in monkeys:
    divisor = divisor * monkey.Test_divisor



for _ in range(10000):
    for monkey in monkeys:
        for item in monkey.Items:
            item = int(item) % divisor
            monkey.Inspection_count +=1
            if monkey.Operand == 'old':  
                item = int(item) * int(item)
            else:
                if monkey.Op == '*':
                    item = int(item)*int(monkey.Operand)
                elif monkey.Op == '+':
                    item = int(item)+int(monkey.Operand)

            if item % monkey.Test_divisor == 0:
                for rcv_monkey in monkeys:
                    if rcv_monkey.Id == monkey.Tcase:
                        rcv_monkey.Items.append(item)
                        break                    
            elif item % monkey.Test_divisor != 0:
                for rcv_monkey in monkeys:
                    if rcv_monkey.Id == monkey.F_case:
                        rcv_monkey.Items.append(item)
                        break
            monkey.Items = monkey.Items[1:]

for monkey in monkeys:
    print (monkey.Inspection_count)

# print(312*320)

t2=t.time()
print(t2-t1)



# for i in range(len(input)):
#     print(input[i])
#     if i % 5 ==0:
#         print()