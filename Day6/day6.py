def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

data = get_input().split('\n\n')

def part_one():
    groups = []
    total_qs = 0
    for d in range(len(data)):
        groups.append(data[d].replace('\n',''))

    for g in range(len(groups)):
        qset = set()
        entry = groups[g]
        for e in entry:
            # sets don't allow duplicate values, perfect for getting unique letters/questions
            qset.add(e)
        total_qs += len(qset)
    print('Questions which anyone answered yes = %s' % total_qs)

def part_two():
    total_qs = 0
    for d in range(len(data)):
        entry = data[d].split()
        qset = set()
        if len(entry) == 1:
            total_qs += len(entry[0])
        else:
            # first get set of unique questions answered
            for e in range(len(entry)):
                for f in range(len(entry[e])):
                    qset.add(entry[e][f])
            qlist = list(qset)
            # check if each unique question is in each group
            for q in qlist:
                valid = 0
                for gr in entry:
                    if q in gr:
                        valid += 1
                if valid == len(entry):
                    total_qs += 1
    print('Questions which everyone answered yes = %s' % total_qs)
            
