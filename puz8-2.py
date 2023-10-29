with open('8r.txt','r') as file:
    file=file.read()


file=file.split()

xlen=len(file[0])
ylen = len(file)

extsum=0
insum=0
sumlist=[]
tmp_ans=1
ans=1
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
        while (ypos -i) >0:  #look up
            utreescore = int(file[ypos-1-i][xpos])
            i+=1    
            if treescore > utreescore:
                if ypos -i ==0:
                    sumlist.append(i)
                    break
                continue
            elif treescore <= utreescore:
                sumlist.append(i)
                break
        i=0
        while (xpos + i) < xlen:  #look right
            rtreescore = int(file[ypos][xpos+1+i])
            i+=1    
            if treescore > rtreescore:
                if xpos + 1+ i == xlen:
                    sumlist.append(i)
                    break    
                continue
            elif treescore <= rtreescore:
                sumlist.append(i)
                break
        
        i=0
        while (ypos + i) < ylen:  #look down
            dtreescore = int(file[ypos+1+i][xpos])
            i+=1    
            if treescore > dtreescore:
                if ypos + 1+ i == ylen:
                    sumlist.append(i)
                    break
                continue
            elif treescore <= dtreescore:
                sumlist.append(i)
                break
  
        i=0
        while (xpos - i) > 0:  #look left
            ltreescore = int(file[ypos][xpos-1-i])
            i+=1    
            if treescore > ltreescore:
                if xpos - i == 0:
                    sumlist.append(i)
                    break
                continue
            elif treescore <= ltreescore:
                sumlist.append(i)
                break

        for num in sumlist:
            tmp_ans = tmp_ans * num
        if tmp_ans >ans:
            ans = tmp_ans
        sumlist=[]
        tmp_ans=1
     

print(ans) # 201684 correct
#first tee baby