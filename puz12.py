with open('12r.txt','r') as input:
    input = input.read().split()

xlen=len(input[0])
ylen = len(input) #8x5 and 179*41
print(xlen,ylen)
#watch for row =0, row = xlen, col =0, col = ylen
#after each exploration, set visited to False for all positions.    -- no, recursion instead
#no need to use 'a'<>'b' -> they can compare directly [b>a=True] 
    #so if nextlet - thisletter [nxt - this <= 1] #might have to use ords for this to write thenm in equations
Startpos=[]

for col in range(ylen):
    # print(input[a])
    for row in range(xlen):
        if input[col][row] == 'S':
            Startpos=(row,col)

        # print(input[col][row],col,row)

print(Startpos)

