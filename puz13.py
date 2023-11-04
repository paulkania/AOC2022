with open('13f.txt','r') as input:
    input=input.read().split()

while input:
    packet1 = input[0]
    packet2 = input[1]

    print(packet1,packet2)

    if type(packet1[0]) == int and type(packet1[1]) == int:
        for digit in minpacket:
            if packet1[0] < packet1[1]:
