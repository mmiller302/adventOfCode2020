#Part two not working, need to redo
def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

data = get_input().split('.\n')
ex_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

part_two_ex = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

data = data_input.split('.\n')
#print(data)

def part_one():
    updated_data = []

    for z in range(len(data)):
        if 'no other bags' not in data[z]:
            updated_data.append(data[z])

    rules = {}
    colors = []

    for d in range(len(updated_data)):
        b = updated_data[d].find('bags')
        colors.append(updated_data[d][:b].strip())
    #print(len(colors))

    for c in colors:
        rules[c] = []
    #print(rules)

    for d in range(len(updated_data)):
        b = updated_data[d].find('bags')
        r = updated_data[d].find('contain')
        bc = updated_data[d][r+7:].strip().split(',')
        bcolors = []
        for a in bc:
            if 'bag' in a:
                f = a.find('bag')
                bcolors.append(a[2:f-1].strip())
            elif 'bags' in a:
                f = a.find('bags')
                bcolors.append(a[2:f-1].strip())
        rules[updated_data[d][:b].strip()] = bcolors

    colors_with_gold = [k for k,v in rules.items() if 'shiny gold' in v]

    new = colors_with_gold
    full_colors_list = colors_with_gold
    colors_set = set()
    for nc in colors_with_gold:
        colors_set.add(nc)

    while len(new) != 0:
        for g in new:
            n = [k for k,v in rules.items() if g in v]
            if len(n) != 0:
                for i in n:
                    full_colors_list.append(i)
                    colors_set.add(i)
            new = n
            #print(colors_set)
        break
    print(len(colors_set))

    #unique_colors = set()
    #for l in full_colors_list:
    #    unique_colors.add(l)
    #print(len(unique_colors))
    
def part_two():
    data = part_two_ex.split('.\n')
    rules = {}
    colors = []

    for d in range(len(data)):
        b = data[d].find('bags')
        colors.append(data[d][:b].strip())
    #print(len(colors))

    for c in colors:
        rules[c] = []
    #print(rules)

    for d in range(len(data)):
        b = data[d].find('bags')
        r = data[d].find('contain')
        bc = data[d][r+7:].strip().split(',')
        bcolors = []
        for a in bc:
            if 'bag' in a:
                f = a.find('bag')
            elif 'bags' in a:
                f = a.find('bags')
            bcolors.append(a[:f-1].strip())
        rules[data[d][:b].strip()] = bcolors
        
    #print(rules)
    shiny_gold_contains = [v for k,v in rules.items() if 'shiny gold' in k]
    print(shiny_gold_contains[0])
    #new = shiny_gold_contains[0]
    full_colors_list = shiny_gold_contains[0]
    
    for z in full_colors_list:
        count_one = z[0]
        color_one = z[2:]
        colors_to_check = rules[color_one]
        new = []
        print(colors_to_check)
        if 'no other bags' in colors_to_check:
            print('color %s does not contain any other bags' % color_one)
        while 'no other bags' not in rules[color_one]:
            for y in colors_to_check:
                count_two = y[0]
                color_two = y[2:]
                if 'no other bags' not in color_two:
                    new = rules[color_two]
                    print(new)
                    colors_to_check = new
                else:
                    break
    
part_one()
#part_two()
