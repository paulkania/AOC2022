#nobody mentions recursion. so good thing i tapped. i had fun making my thing kind of work sort of
#getting better at working with functions
#work on replace 'S','a;'
#work on understanding how global vars and vars work across functions
#why did score =-1 get fucked while score = score -1 work fine?

#ALSO CHANGE E COORD, IT IS HARDCODED
with open('12f.txt','r') as input: 
    input = input.read().split()
#ALSO CHANGE E COORD, IT IS HARDCODED

xlen=len(input[0])
ylen = len(input) #8x5 and 179*41

location_dict={}
score_dict={}
for colx in range(ylen):
    for rowy in range(xlen):
        location_dict[(colx,rowy)] = False
        score_dict[(colx,rowy)] = 1000000000 #infinite
        if input[colx][rowy] == 'S': # 0,0 and 20,0
            start_x, start_y = colx, rowy
            location_dict[(colx,rowy)] = True #
        if input[colx][rowy] == 'E': #11f 2,5(DOWN 2, RIGHT 5), 12r-> 20 down, 154 right
            end_x,end_y = colx, rowy



    

scores=[]
global score
score=0
options=[] # rowpos, colpos  = options[-1][0][0] options[-1][0][1] 
current_path=[]
score_string=''
endjump = True


def check_for_peak(x,y,rowp,colp):
    global endjump
    global score
    endjump = True
    if input[rowp+x][colp+y] == 'E' and not (input[rowp][colp] == 'y' or input[rowp][colp] == 'z'):
        endjump = False
    elif input[rowp+x][colp+y] == 'E' and (input[rowp][colp] == 'y' or input[rowp][colp] == 'z'):
        score+=1
        scores.append(score)
        return scores
    return endjump

def look_around(rowp,colp):

    global current_path
    global score
    global score_string
    current_path.append([rowp,colp]) #y,x
    #this might not work because the first way there might not be the fastest and only way
    if rowp-1 >= 0: #look UP?
        if location_dict[(rowp-1,colp)]== False: 
            if (ord(input[rowp-1][colp]) - ord(input[rowp][colp])  < 2) or ((input[rowp][colp])) == 'S':
                Endjump = check_for_peak(-1,0,rowp,colp)
                if Endjump == True:
                    score +=1
                    score_string+=input[rowp-1][colp]
                    location_dict[(rowp-1,colp)] = True
                    look_around(rowp-1,colp)
                elif Endjump == False:
                    endjump = True
    if rowp+1 < ylen:#look DOWN
        if location_dict[(rowp+1,colp)]== False: 
            if (ord(input[rowp+1][colp]) - ord(input[rowp][colp]) < 2) or ((input[rowp][colp])) == 'S':
                Endjump = check_for_peak(+1,0,rowp,colp)
                if Endjump == True:                
                    score +=1
                    score_string+=input[rowp+1][colp]
                    location_dict[(rowp+1,colp)] = True
                    look_around(rowp+1,colp)
                elif Endjump == False:
                    endjump = True
    if colp-1 >= 0: # look LEFT? 
        if location_dict[(rowp,colp-1)]== False: 
            if (ord(input[rowp][colp-1]) - ord(input[rowp][colp]) < 2) or ((input[rowp][colp])) == 'S':
                Endjump = check_for_peak(0,-1,rowp,colp)
                if Endjump == True:                
                    score +=1
                    score_string+=input[rowp][colp-1]
                    location_dict[(rowp,colp-1)] = True
                    look_around(rowp,colp-1)
                elif Endjump == False:
                    endjump = True
    if colp+1 < xlen: #look Right
        if location_dict[(rowp,colp+1)]== False: 
            if (ord(input[rowp][colp+1]) - ord(input[rowp][colp]) < 2) or ((input[rowp][colp])) == 'S':
                Endjump = check_for_peak(0,1,rowp,colp)
                if Endjump == True:                
                    score +=1
                    score_string+=input[rowp][colp+1]
                    location_dict[(rowp,colp+1)] = True
                    look_around(rowp,colp+1)
                elif Endjump == False:
                    endjump = True
    current_path= current_path[0:-1]
    score = score - 1 #this works, whilke score -= 1 does not.
    look_around(current_path[-1][0][0],current_path[-1][0][1]) 



# for k,v in location_dict.items():
#     print(k,v,tcolpe(k))



