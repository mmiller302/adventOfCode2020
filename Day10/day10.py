#didn't do part two yet

from collections import Counter

def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

data = get_input().splitlines()

data_sorted = []
data_sorted.append(0)
for i in data:
    data_sorted.append(int(i))

ds = sorted(data_sorted)

def part_one():
    diffs = []
    
    for j in range(len(ds)-1):
        diff = ds[j+1] - ds[j]
        diffs.append(diff)

    #last adapter has +3 capacity
    diffs.append(3)

    counts = Counter(diffs)
    print(counts)
    
def part_two():
    pass
    
#part_one()
part_two() 
