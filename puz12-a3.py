# with open('12f.txt','r') as input:
#     input = input.read().split()

# xlen=len(input[0])
# ylen = len(input) #8x5 and 179*41

# location_dict={}
# score_dict={}
# for colx in range(ylen):
#     # print(input[a])
#     for rowy in range(xlen):
#         location_dict[(colx,rowy)] = False
#         score_dict[(colx,rowy)] = 1000000000 #infinite
#         if input[colx][rowy] == 'S':
#             start_x, start_y = colx, rowy
#             location_dict[(colx,rowy)] = True #

# scores=[]
# score=0
# options=[] # xpos, ypos  = options[-1][0][0] options[-1][0][1] 
# def look_around(xp,yp):
#     global score
#     if input[xp][yp]== 'E':
#         scores.append(score) #this might not work because the first way there might not be the fastest and only way
#     if xp-1 > 0:
#         if location_dict[(xp-1,yp)]== False: #look left
#             if (ord(input[xp-1][yp]) - ord(input[xp][yp])  < 2) or ((input[xp][yp])) == 'S' :
#                 score +=1
#                 location_dict[(xp-1,yp)] = True
#                 options.append([xp-1,yp])
#     if xp+1 < xlen:
#         if location_dict[(xp+1,yp)]== False: #look right
#             if (ord(input[xp+1][yp]) - ord(input[xp][yp]) < 2) or ((input[xp][yp])) == 'S':
#                 score +=1
#                 location_dict[(xp+1,yp)] = True
#                 options.append([xp+1,yp])
#     if yp-1 > 0:
#         if location_dict[(xp,yp-1)]== False: # look up
#             if (ord(input[xp+1][yp]) - ord(input[xp][yp]) < 2) or ((input[xp][yp])) == 'S':
#                 score +=1
#                 location_dict[(xp,yp-1)] = True
#                 options.append([xp,yp-1])
#     if yp+1 < ylen:
#         if location_dict[(xp,yp+1)]== False: #look down
#             if (ord(input[xp+1][yp]) - ord(input[xp][yp]) < 2) or ((input[xp][yp])) == 'S':
#                 score +=1
#                 location_dict[(xp,yp+1)] = True
#                 options.append([xp,yp+1])
#                 look_around(xp,yp+1)
#     score=0 #nothing found, go to start and try again
#     look_around(start_x,start_y)

# look_around(start_x,start_y)    
# print(scores)


# # for k,v in location_dict.items():
# #     print(k,v,type(k))



