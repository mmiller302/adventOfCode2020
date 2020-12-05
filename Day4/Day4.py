#solves puzzle but needs cleaning up

def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
hcl_fields = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_passports(validation=False):    
    data = get_input().split('\n\n')
    passports = []
    valid_entries = 0

    for p in range(len(data)):
        passports.append(data[p].replace('\n',' '))
    
    for i in range(len(passports)):
        entry = passports[i].split()
        if validation:
            if policy_check(entry):
                valid_entries += 1
        else:
            valid = 0
            for e in range(len(entry)):
                #TODO: switch to using 'all' + list comprehension for this 
                if entry[e].split(':')[0] in fields:
                    valid += 1
            if valid >= 7:
                valid_entries += 1
            
def policy_check(data_entry):
    valid_fields = []
    valid_hcl = []
    p_valid = False
    if len(data_entry) >= 7:
        for a in range(len(data_entry)):
            field = (data_entry[a]).split(':')[0]
            value = (data_entry[a]).split(':')[1]
            if field in fields:
                if 'byr' in field and len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
                    valid_fields.append(field)
                elif 'iyr' in field and len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
                    valid_fields.append(field)
                elif 'eyr' in field and len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
                    valid_fields.append(field)
                elif 'hgt' in field:
                    if 'cm' in value or 'in' in value[-2:]:
                        if 'cm' in value:
                            if int(value.strip('cm')) >= 150 and int(value.strip('cm')) <= 193:
                                valid_fields.append(field)
                        elif 'in' in value:
                            if int(value.strip('in')) >= 59 and int(value.strip('in')) <= 76:
                                valid_fields.append(field)
                elif 'hcl' in field:
                    if '#' in value[0] and len(value) == 7:
                        for s in value:
                            if s in hcl_fields:
                                valid_hcl.append(s)
                        if len(valid_hcl) == 6:
                            valid_fields.append(field)
                elif 'ecl' in field:
                    if value in colors:
                        valid_fields.append(field)
                elif 'pid' in field and len(value) == 9:
                    valid_fields.append(field)
        if len(valid_fields) == len(fields):
            return True
    return False
    
check_passports(False)
check_passports(True)
