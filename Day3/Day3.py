#might be ugly but it works

def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

t = get_input().splitlines()

def trees(right,down):
    num_trees = 0
    start = 0
    n_line = ""
    for i in range(1,len(t),down):
        while i < len(t)-down:
            if i == 1:
                f_line = t[1]
            else:
                f_line = n_line
            n_line = t[t.index(f_line)+down]
        
            #reached a point where we'll go beyond the line length, adjust start position accordingly
            if start >= (len(f_line) - right):
                start = right - (len(f_line) - start)                
            else:
                start += right
            move_down = n_line[start]
            if '#' in move_down:
                    num_trees += 1
            break
    print('Slope is R%s, D%s. Trees = %s' % (right,down,num_trees))
    
