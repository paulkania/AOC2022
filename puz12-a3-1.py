import collections
#nobody mentions recursion. so good thing i tapped. i had fun making my thing kind of work sort of
#getting better at working with functions
    #specifaclly: work on understanding how global vars and vars work across functions
#work on replace 'S','a;'
#why did score =-1 get fucked while score = score -1 work fine?

with open('12f.txt','r') as input: ###CHANGE START_POS AND END_POS
    input = input.read().split()

columns=len(input[0])
rows = len(input) #8x5 and 179*41
score=0

start_position = [0,0] # [20,0] for r !!!
end_position = [5,2] #5R 2Down. For R: [154,20] !!!
grid = [[0] * columns for _ in range(rows)]

visit_dict={}
for row in range(rows): #col gives x, row gives y
    for col in range(columns):
        visit_dict[(row,col)]= False

visit_dict[(0,0)]= True #!!! change for R
Q = collections.deque([[0,0]]) #


score=1
appended=0
cycles=[1]
rnd=0
while Q:
    rnd+=1
    current_position = Q.popleft()#[row,col]
    rowp = current_position[0]
    colp = current_position[1]
    if cycles[0] > 0:
        cycles[0]= cycles[0] -1
    elif cycles[0] ==0:
        score+=1
        cycles=cycles[1:]
        cycles[0]= cycles[0] -1

    cp_score = ord(input[rowp][colp])
    if rowp-1 >= 0 and visit_dict[(rowp-1,colp)] == False: #look UP?
            if (ord(input[rowp-1][colp]) - cp_score)  < 2:
                if input[rowp-1][colp] == [5,2]:
                    print(score,'score')
                    break
                else:
                    appended +=1 #may be extraneous
                    grid[rowp-1][colp] = score
                    Q.append([rowp-1,colp])
                    visit_dict[(rowp-1,colp)] = True
    if rowp+1 < rows and visit_dict[(rowp+1,colp)] == False: #look DOWN
       if (ord(input[rowp+1][colp]) - cp_score)  < 2:
                if input[rowp+1][colp] == [5,2]:
                    print(score,'score')
                    break
                else:
                    appended +=1
                    grid[rowp+1][colp] = score
                    Q.append([rowp+1,colp])
                    visit_dict[(rowp+1,colp)] = True
    if colp-1 >= 0 and visit_dict[(rowp,colp-1)] == False: # look LEFT? 
        if (ord(input[rowp][colp-1]) - cp_score  < 2):
                if input[rowp][colp-1] == [5,2]:
                    print(score,'score')
                    break
                else:
                    appended +=1
                    grid[rowp][colp-1] = score
                    Q.append([rowp,colp-1])
                    visit_dict[(rowp,colp-1)] = True
    if colp+1 < columns and visit_dict[(rowp,colp+1)] == False: #look Right
        if (ord(input[rowp][colp+1]) - cp_score  < 2):
            if input[rowp][colp+1] == [5,2]:
                print(score,'score')
                break
            else:
                appended +=1
                grid[rowp][colp+1] = score
                Q.append([rowp,colp+1])
                visit_dict[(rowp,colp+1)] = True
    if appended == 0:
         score -= 1
    cycles.append(appended)
    appended=0





