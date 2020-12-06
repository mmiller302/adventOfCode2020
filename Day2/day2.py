from collections import Counter

def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

data = get_input().split()

def part_one():
    valid = 0
    for p in range(len(data)):
        entry = data[p].split()
        policy = entry[0]
        dash = policy.find('-')
        min_req = policy[:dash]
        max_req = policy[dash+1:]
        
        letter = entry[1].strip(':')
        
        password = entry[2]
        
        if letter in password:
            counts = Counter(password)
            if counts[letter] >= int(min_req) and counts[letter] <= int(max_req):
                valid += 1
    
    print('Part 1: %s' % valid)        

def part_two():
    valid = 0
    for p in range(len(data)):
        entry = data[p].split()
        policy = entry[0]
        dash = policy.find('-')
        min_req = policy[:dash]
        max_req = policy[dash+1:]
        
        letter = entry[1].strip(':')
        
        password = entry[2]

        if letter in password:
            c1 = password[int(min_req) -1]
            c2 = password[int(max_req) -1]
            if (letter in c1) ^ (letter in c2):
                valid += 1
    
    print('Part 2: %s' % valid)
    
