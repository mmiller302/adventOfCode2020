def get_input():
    with open('input.txt', 'r') as input_file:
        input = input_file.read()
    return input

seats = get_input().splitlines()

def row(row_data):
    position = []
    row_positions = [rw for rw in range(128)]
    for r in range(len(row_data)):
        # F means take LOWER half of data e.x. 0 - 63
        if 'F' in row_data[r]:
            if r == 0:
                position = row_positions[:(int(len(row_positions)/2))]
            else:
                position = position[:(int(len(position)/2))]
        # B means take UPPER half of data e.x. 64 - 127
        else:
            if r == 0:
                position = row_positions[(int(len(row_positions)/2)):]
            else:
                position = position[(int(len(position)/2)):]
    return position[0]

def column(column_data):
    position = []
    column_positions = [cw for cw in range(8)]
    for r in range(len(column_data)):
        # L means take LOWER half of data e.x. 0 - 3
        if 'L' in column_data[r]:
            if r == 0:
                position = column_positions[:(int(len(column_positions)/2))]
            else:
                position = position[:(int(len(position)/2))]
        # R means take UPPER half of data e.x. 4 - 7
        else:
            if r == 0:
                position = column_positions[(int(len(column_positions)/2)):]
            else:
                position = position[(int(len(position)/2)):]
    return position[0]

def max_seat_id():
    seat_ids = []
    for s in range(len(seats)):
        row_num = row(seats[s][:7])
        column_num = column(seats[s][7:])
        seat_ids.append((row_num * 8) + column_num)
    print('Max seat id is %s' % max(seat_ids))

def my_seat():
    seat_dict = {}
    columns = {0,1,2,3,4,5,6,7}
    rows = range(128)
    for r in rows:
        seat_dict[r] = []
    for s in range(len(seats)):
        row_num = row(seats[s][:7])
        column_num = column(seats[s][7:])
        seat_dict[row_num].append(column_num)
    for num in rows:
        # any row with less than 7 seats filled is likely at the very front or back of the plane
        # prompt says my seat is not at very front or very back
        # change 'if' to != 8 and you can see each of those rows
        if len(seat_dict[num]) == 7:
            missing_column = columns.difference(set(sorted(seat_dict[num])))
            #print('Row %s is missing seats, seats are %s' % (num,seat_dict[num]))          
            print('My seat id is %s' % ((num * 8) + missing_column.pop()))
            
