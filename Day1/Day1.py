def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

data = get_input().splitlines()

def part_one():
    for d in range(len(data)):
        for e in range(len(data)):
            if (int(data[d]) + int(data[e]) == 2020):
                print('Found them! %s + %s = 2020' % (data[d],data[e]))

def part_two():
    for d in range(len(data)):
        for e in range(len(data)):
            for f in range(len(data)):
                if (int(data[d]) + int(data[e]) + int(data[f]) == 2020):
                    print('Found them! %s + %s + %s = 2020' % (data[d],data[e],data[f]))
                    
