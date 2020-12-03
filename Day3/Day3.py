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
            fidx = r.index(fline)
            nline = r[fidx+down]
        
            if start >= (len(fline) - right):
                fline = nline
                start = right - (len(fline) - start)
                move_down = fline[start]                
            else:
                line_start = fline[start]
                start += right
                move_right = fline[start]
                move_down = nline[start]
            if '#' in move_down:
                    num_trees += 1
            break
    print('Slope is R%s, D%s. Trees = %s' % (right,down,num_trees))
