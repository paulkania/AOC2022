with open('8f.txt','r') as file:
    file=file.read()


file=file.split()

xlen=len(file[0])
ylen = len(file)

extsum=0
insum=0
corner_cases4 =[]
debug_ans=[]
for xpos in range(0,xlen):
    for ypos in range(0,ylen):
        if (ypos == 0 or xpos == 0) or (ypos == ylen-1 or xpos == xlen-1):
            extsum +=1
            continue
        tree = int(file[xpos][ypos])
        utree = int(file[xpos-1][ypos])
        dtree = int(file[xpos+1][ypos])
        ltree = int(file[xpos][ypos-1])
        rtree = int(file[xpos][ypos+1])
        if (xpos == 1 and ypos == 1) or (xpos == xlen-2 and ypos == 1) or (xpos == 1 and ypos == ylen-2) or ((xpos == xlen-2 and ypos == ylen-2)):
            #tl,tr,bl,br
            print(tree,utree,rtree,dtree,ltree)
            continue

        if xpos ==1: #top horizontal line
            if tree > utree:
                debug_ans.append([tree,utree,rtree,dtree,ltree])
                insum +=1
                continue
        if xpos == xlen-2: # bottom horizontal line
            if tree > dtree:
                debug_ans.append([tree,utree,rtree,dtree,ltree])
                insum +=1
                continue
        if ypos ==1: #look left
            if tree > ltree:
                insum +=1
                debug_ans.append([tree,utree,rtree,dtree,ltree])
                continue
        if ypos == ylen-2: #right side, vert line, look right
            if tree > rtree:
                insum +=1
                debug_ans.append([tree,utree,rtree,dtree,ltree])
                continue
        if tree > utree:
            if tree > dtree:
                if tree > ltree:
                    if tree > rtree:
                        insum+=1
                        continue

print(extsum,insum)
print(debug_ans)