def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

data = get_input().splitlines()

preamble = 25

def part_one():
    for i in range(preamble,len(data)):
        nums_to_sum = data[i-preamble:i]
        found_sum = False
        for g in nums_to_sum:
            for h in nums_to_sum:
                if int(g) + int(h) == int(data[i]):
                    found_sum = True
        if not found_sum:
            print('Invalid num = %s' % data[i])
            return data[i]
    
def part_two(inv_num):
    #print(inv_num)
    nums_tried = []
    for i in range(len(data)):
        seed = int(data[i])
        next_idx = i + 1
        num_sum = seed + int(data[next_idx])
        nums_tried.append(data[i])
        nums_tried.append(data[next_idx])
        
        while num_sum < int(inv_num):
            next_idx += 1
            num_sum += int(data[next_idx])
            nums_tried.append(data[next_idx])
        if num_sum > int(inv_num):
            nums_tried = []
            continue
        else:
            #print('Found contiguous nums!')
            break

    weakness = int(min(nums_tried)) + int(max(nums_tried))
    print('Weakness = %s' % weakness)
    
inv_num = part_one()
part_two(inv_num)
