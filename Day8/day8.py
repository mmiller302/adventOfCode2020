#very messy, want to clean up

ex_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

data = data_input.split('\n')
#print(data)

move_map = {}
for a in range(len(data)):
    move_map[a] = data[a]

#print(move_map)

def part_one():
    accumulator = 0
    instruction = move_map[0]
    new_instruction = instruction
    pos = 0
    next_hop = 0
    positions_visited = []

    while pos not in positions_visited:
        #print('pos right inside while is %s' % pos)
        if 'nop' in new_instruction :
            #print('pos is %s' % pos)
            positions_visited.append(pos)

            next_hop = 1
            new_instruction = move_map[pos+next_hop]
            pos += next_hop 
            
           # print('pos after hop is %s' % pos)
            #print('new instruction is %s' % new_instruction)
            #print(positions_visited)
            
        if 'acc' in new_instruction :
            #print('pos is %s' % pos)
            tmp = move_map[pos]
            #print('tmp is %s' % move_map[pos])
            positions_visited.append(pos)
            if '+' in tmp:
                direction = tmp.find('+')
                add_to_accum = tmp[direction+1:]
                accumulator += int(add_to_accum)
            else:
                direction = tmp.find('-')
                add_to_accum = tmp[direction+1:]
                accumulator -= int(add_to_accum)
                
            next_hop = 1
            new_instruction = move_map[pos+next_hop]
            pos += next_hop
            
            #print('pos after hop is %s' % pos)
            #print('new instruction is %s' % new_instruction)
            #print(positions_visited)
            #print('accumulator = %s' % accumulator)

        if 'jmp' in new_instruction:
            #print('pos is %s' % pos)
            positions_visited.append(pos)
            tmp = move_map[pos]
            #print('tmp is %s' % move_map[pos])
            if '+' in tmp:
                direction = tmp.find('+')
                jump_move = tmp[direction+1:]
                #print('jump move is %s' % jump_move)
                new_instruction = move_map[pos+int(jump_move)]
                pos += int(jump_move)
            else:
                direction = tmp.find('-')
                jump_move = tmp[direction+1:]
                #print('jump move is %s' % jump_move)
                new_instruction = move_map[pos-int(jump_move)]
                pos -= int(jump_move)
                
            #print('pos after hop is %s' % pos)
            #print('new instruction is %s' % new_instruction)
            #print(positions_visited)
    print('accumlator at point of repeat was %s' % accumulator)
    return positions_visited
    
def part_two(positions_tried):
    moves_made = positions_tried

    instruction = move_map[0]

    for r in range(len(moves_made)):
        entry_num = moves_made[r]
        tmp_entry = move_map[entry_num]
        print('Trying entry %s' % entry_num)
        mv = move_map[entry_num].split()[1]
        if 'nop' in move_map[entry_num]:           
            move_map[entry_num] = 'jmp ' + mv
        if 'jmp' in move_map[entry_num]:
            move_map[entry_num] = 'nop ' + mv
        #correct_move_to_change,correct,acc = run_through_data(entry_num,move_map[entry_num])
        #if correct:
        #    print('Change %s!' % correct_move_to_change)
        #    print('Accumulator at end was %s' % acc)
        #    break
        correct = run_through_data(entry_num,move_map)
        move_map[entry_num] = tmp_entry

def run_through_data(entry, new_instruction):    
    accumulator = 0
    pos = 0
    next_hop = 0
    positions_visited = []
    correct_move_to_change = 0
    second_to_last = False
    new_instruction = move_map[0]
    while pos not in positions_visited:
    #while pos != len(move_map) - 2:
        print('pos right inside while is %s' % pos)
        if 'nop' in new_instruction :
            if pos == len(move_map) - 2 and not second_to_last:
                print('Got to second to last instruction! %s' % new_instruction) 
                new_instruction = 'jmp +1'
                second_to_last = True
                
            else:
                print('pos is %s' % pos)
                positions_visited.append(pos)
                next_hop = 1
                
                if pos == len(move_map):
                    print('All done! At the end.')
                elif pos < len(move_map) - next_hop:
                    new_instruction = move_map[pos+next_hop]
                    pos += next_hop
            
                print('pos after hop is %s' % pos)
                print('new instruction is %s' % new_instruction)
                #print(positions_visited)
            
        if 'acc' in new_instruction :
            print('pos is %s' % pos)
            tmp = move_map[pos]
            print('tmp is %s' % move_map[pos])
            positions_visited.append(pos)
            if '+' in tmp:
                direction = tmp.find('+')
                add_to_accum = tmp[direction+1:]
                accumulator += int(add_to_accum)
            else:
                direction = tmp.find('-')
                add_to_accum = tmp[direction+1:]
                accumulator -= int(add_to_accum)
            next_hop = 1
            if pos == len(move_map):
                print('All done! At the end.')
            elif pos < len(move_map) - next_hop:
                new_instruction = move_map[pos+next_hop]
                pos += next_hop

            print('pos after hop is %s' % pos)
            print('new instruction is %s' % new_instruction)
            #print(positions_visited)
            print('accumulator = %s' % accumulator)

        if 'jmp' in new_instruction:
            if pos == len(move_map) - 2 and not second_to_last:
                print('Got to second to last instruction! %s' % new_instruction) 
                new_instruction = 'nop +0'
                second_to_last = True  
            else:
                tmp = move_map[pos]
                print('pos is %s' % pos)
                positions_visited.append(pos)
            
                print('tmp is %s' % move_map[pos])
                if '+' in tmp:
                    direction = tmp.find('+')
                    jump_move = tmp[direction+1:]
                    #print('jump move is %s' % jump_move)
                    if pos == len(move_map):
                        print('All done! At the end.')
                    elif pos < len(move_map) - 2:
                        new_instruction = move_map[pos+int(jump_move)]
                        pos += int(jump_move)
                else:
                    direction = tmp.find('-')
                    jump_move = tmp[direction+1:]
                    #print('jump move is %s' % jump_move)
                    if pos == len(move_map):
                        print('All done! At the end.')
                    elif pos < len(move_map) - 2:
                        new_instruction = move_map[pos-int(jump_move)]
                        pos -= int(jump_move)
                
                print('pos after hop is %s' % pos)
                print('new instruction is %s' % new_instruction)
                #print(positions_visited)
        if second_to_last:
            print('Got a second to last')
            return True
    #print('accumlator at end was %s' % accumulator)

pvisited = part_one()
part_two(pvisited)
