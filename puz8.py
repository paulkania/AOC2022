with open('8r.txt','r') as file:
    file=file.read()


file=file.split()

xlen=len(file[0])
ylen = len(file)

extsum=0
insum=0
corner_cases4 =[]
debug_ans=[]
for ypos in range(0,xlen):
    for xpos in range(0,ylen):
        if (xpos == 0 or ypos == 0) or (xpos == ylen-1 or ypos == xlen-1):
            extsum +=1
            continue
        treescore = int(file[ypos][xpos])
        utreescore = int(file[ypos-1][xpos])
        dtreescore = int(file[ypos+1][xpos])
        ltreescore = int(file[ypos][xpos-1])
        rtreescore = int(file[ypos][xpos+1])
        
        
        i=0
        found=False
        while (ypos -i) >0 and found == False:  #look up
            utreescore = int(file[ypos-1-i][xpos])
            i+=1    
            if treescore > utreescore:
                if ypos -i ==0:
                    insum+=1
                    found = True
                    break
            elif treescore <= utreescore:
                break

        i=0
        while (xpos + i) < xlen and found == False:  #look right
            rtreescore = int(file[ypos][xpos+1+i])
            i+=1    
            if treescore > rtreescore:
                if xpos + 1+ i == xlen:
                    insum+=1
                    found = True
                    break
            elif treescore <= rtreescore:
                break

        i=0
        while (ypos + i) < ylen and found == False:  #look down
            dtreescore = int(file[ypos+1+i][xpos])
            i+=1    
            if treescore > dtreescore:
                if ypos + 1+ i == ylen:
                    insum+=1
                    found = True
                    break
            elif treescore <= dtreescore:
                break
  
        i=0
        while (xpos - i) > 0 and found == False:  #look left
            ltreescore = int(file[ypos][xpos-1-i])
            i+=1    
            if treescore > ltreescore:
                if xpos - i == 0:
                    insum+=1
                    break
            elif treescore <= ltreescore:
                break

     

print(extsum,insum)
print(extsum+insum) #21,1681 part 1.