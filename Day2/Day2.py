#passwords is just the string rep of input.txt

from collections import Counter

psplit = passwords.split()

def part1():
    valid = 0
    for r in range(0,len(psplit),3):
        policy = psplit[r]
        dash = policy.find('-')
        min_req = policy[:dash]
        max_req = policy[dash+1:]
        letter_req = psplit[r+1][0]
        pwd = psplit[r+2]

        if letter_req in pwd:
            counts = Counter(pwd)
            if counts[letter_req] >= int(min_req) and counts[letter_req] <= int(max_req):
                valid += 1
    
    print('Part 1: %s' % valid)            

def part2():
    valid = 0
    for r in range(0,len(psplit),3):
        policy = psplit[r]
        dash = policy.find('-')
        min_req = policy[:dash]
        max_req = policy[dash+1:]
        letter_req = psplit[r+1][0]
        pwd = psplit[r+2]

        if letter_req in pwd:
            c1 = pwd[int(min_req) -1]
            c2 = pwd[int(max_req) -1]
            if (letter_req in c1) ^ (letter_req in c2):
                valid += 1
    
    print('Part 2: %s' % valid)
