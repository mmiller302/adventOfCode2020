#passwords is just the string rep of input.txt

from collections import Counter

psplit = passwords.split()

def part1():
    valid = 0
    for r in range(0,len(psplit),3):
        entry = psplit[r]
        dash = entry.find('-')
        min_req = entry[:dash]
        max_req = entry[dash+1:]
        letter_req = psplit[r+1]
        l = letter_req[0]
        pwd = psplit[r+2]

        if l in pwd:
            counts = Counter(pwd)
            if counts[l] >= int(min_req) and counts[l] <= int(max_req):
                valid += 1
    
    print(valid)            

def part2():
    valid = 0
    for r in range(0,len(psplit),3):
        entry = psplit[r]
        dash = entry.find('-')
        min_req = entry[:dash]
        max_req = entry[dash+1:]
        letter_req = psplit[r+1]
        l = letter_req[0]
        pwd = psplit[r+2]

        if l in pwd:
            c1 = pwd[int(min_req) -1]
            c2 = pwd[int(max_req) -1]
            if (l in c1) ^ (l in c2):
                valid += 1
    
    print(valid)
    
part1()
part2()
