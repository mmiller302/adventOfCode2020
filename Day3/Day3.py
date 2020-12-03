#this is pretty ugly but it works

r = tree_map.splitlines()

def trees(right,down):
    num_trees = 0
    start = 0
    nline = ""
    for i in range(1,len(r),down):
        while i < len(r)-down:
            if i == 1:
                fline = r[1]
            else:
                fline = nline
            nline = r[r.index(fline)+down]
        
            #reached a point where we'll go beyond the line length, adjust start position accordingly
            if start >= (len(fline) - right):
                start = right - (len(fline) - start)                
            else:
                start += right
            move_down = nline[start]
            if '#' in move_down:
                    num_trees += 1
            break
    print('Slope is R%s, D%s. Trees = %s' % (right,down,num_trees))
    
