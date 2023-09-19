

INFILE = 'test_input.txt'
#INFILE = 'puzzle_input.txt'
#INFILE = '/Users/mattcriswell/github/adventofcode2022/day09/puzzle_input.txt'

#GRID_SIZE = 10
GRID_SIZE = 10
OFFSET=0
#GRID_SIZE = 2000

class LostHead(Exception): pass

# make grid structure
tail_moves = []
grid = [['.' for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

def show_grid():
    print("")
    for row in grid:
        print(row)
    print("")


def move_tail(instruction):
    verb = instruction[0]
    distance = int(instruction[1])

    if verb == 'R':
            print('move tail right')
            prior_val = grid[tail_coords['y']][tail_coords['x'] + 1]   
            if prior_val == 'H':
                #no move
                return None             
            grid[tail_coords['y']][tail_coords['x']] = 'x'
            tail_coords['x'] += 1

    if verb == 'L':
            print('move tail left')
            prior_val = grid[tail_coords['y']][tail_coords['x'] - 1] 
            if prior_val == 'H':
                #no move
                return None 
            grid[tail_coords['y']][tail_coords['x']] = 'x'
            tail_coords['x'] -= 1  
            if not prior_val == 'H':
                grid[tail_coords['y']][tail_coords['x']] = 'T'                     

    if verb == 'U':
            print('move tail up')
            prior_val = grid[tail_coords['y'] + 1][tail_coords['x']]
            if prior_val == 'H':
                #no move
                return None 
            grid[tail_coords['y']][tail_coords['x']] = 'x'
            tail_coords['y'] += 1
            if not prior_val == 'H':
                grid[tail_coords['y']][tail_coords['x']] = 'T'            
                 
    if verb == 'D':
            print('move tail down')
            prior_val = grid[tail_coords['y'] - 1][tail_coords['x']]
            if prior_val == 'H':
                #no move
                return None 
            grid[tail_coords['y']][tail_coords['x']] = 'x'
            tail_coords['y'] -= 1
            if not prior_val == 'H':
                grid[tail_coords['y']][tail_coords['x']] = 'T'        
           
    tail_moves.append(tuple(tail_coords.values()))
            

def move_head(instruction):
    verb = instruction[0]
    distance = int(instruction[1])
    for hop in range(distance):

        if verb == 'R':
            print('move right')
            prior_val = grid[head_coords['y']][head_coords['x'] + 1]
            if grid[head_coords['y']][head_coords['x']] == 'H':
                grid[head_coords['y']][head_coords['x']] = prior_val
            else:
                raise Exception(LostHead)
            head_coords['x'] += 1
            grid[head_coords['y']][head_coords['x']] = 'H'
            tail_follow()

        if verb == 'L':
            print('move left')
            prior_val = grid[head_coords['y']][head_coords['x'] - 1]
            if grid[head_coords['y']][head_coords['x']] == 'H':
                grid[head_coords['y']][head_coords['x']] = prior_val
            else:
                raise Exception(LostHead)
            head_coords['x'] -= 1
            grid[head_coords['y']][head_coords['x']] = 'H'
            tail_follow()

        if verb == 'U':
            print('move up')
            prior_val = grid[head_coords['y'] + 1][head_coords['x']]
            if grid[head_coords['y']][head_coords['x']] == 'H':
                grid[head_coords['y']][head_coords['x']] = prior_val
            else:
                raise Exception(LostHead)
            head_coords['y'] += 1
            grid[head_coords['y']][head_coords['x']] = 'H'
            tail_follow()         

        if verb == 'D':
            print('move down')
            prior_val = grid[head_coords['y'] - 1][head_coords['x']]
            if grid[head_coords['y']][head_coords['x']] == 'H':
                grid[head_coords['y']][head_coords['x']] = prior_val
            else:
                raise Exception(LostHead)
            head_coords['y'] -= 1
            grid[head_coords['y']][head_coords['x']] = 'H'
            tail_follow()


def tail_x_closer():
    # head horizontally too far
    if head_coords['x'] > tail_coords['x']:
        # move right
        move_tail(['R', 1])
    else:
        # move left
        move_tail(['L', 1])

def tail_y_closer():
    # head vertically too far
    if head_coords['y'] > tail_coords['y']:
        #move up
        move_tail(['U', 1])
    else:
        #move down
        move_tail(['D', 1])


def tail_follow():
    ''' calculate where the tail should be based on the current position of head '''
    # tail_coords = {'y':0,'x':0}
    y_diff = abs(head_coords['y'] - tail_coords['y'])
    x_diff = abs(head_coords['x'] - tail_coords['x'])

    # if x_diff <= 1 and y_diff <= 1:
    #     return None

    if y_diff >= 2 and x_diff == 2:
        tail_x_closer()
        tail_y_closer()
        return None

    elif x_diff >= 2 and y_diff == 2:
        tail_y_closer()
        tail_x_closer()
        return None
    
    if x_diff == 2 and y_diff <= 1:
        tail_x_closer()
        return None
    if y_diff == 2 and x_diff <= 1:
        tail_y_closer()
        return None


    # if head_coords['y'] == tail_coords['y'] and head_coords['x'] == tail_coords['x']:
    #     # head sitting on tail nothing to do
    #     pass
#    # if y_diff > 1 and x_diff > 1:
#         if head_coords['y'] > tail_coords['y']:
#             #move up
#             move_tail(['U', 1])
#         else:
#             #move down
#             move_tail(['D', 1])
#         if head_coords['x'] > tail_coords['x']:
#             # move right
#             move_tail(['R', 1])
#         else:
#             # move left
#             move_tail(['L', 1])
#         return None
        
        # within tolerance so no movement required
        #pass
    # if y_diff >= 1:
    #     # head vertically too far
    #     if head_coords['y'] > tail_coords['y']:
    #         #move up
    #         move_tail(['U', 1])
    #     else:
    #         #move down
    #         move_tail(['D', 1])
    #     if x_diff >= 1:
    #         # head horizontally too far
    #         if head_coords['x'] > tail_coords['x']:
    #             # move right
    #             move_tail(['R', 1])
    #         else:
    #             # move left
    #             move_tail(['L', 1])
    #     return None

    # if x_diff >= 1:
    #     # head horizontally too far
    #     if head_coords['x'] > tail_coords['x']:
    #         # move right
    #         move_tail(['R', 1])
    #     else:
    #         # move left
    #         move_tail(['L', 1])
    #     if y_diff >= 1:
    #     # head vertically too far
    #         if head_coords['y'] > tail_coords['y']:
    #             #move up
    #             move_tail(['U', 1])
    #         else:
    #             #move down
    #             move_tail(['D', 1])
    #     return None


# read instructions
#with open('test_input.txt', 'rt') as in_file:
#with open('puzzle_input.txt', 'rt') as in_file:
#with open('/Users/mattcriswell/github/adventofcode2022/day09/puzzle_input.txt', 'rt') as in_file:
with open(INFILE, 'rt') as in_file:
    contents = in_file.read().strip()

instructions = []
for i in contents.split('\n'):
    instructions.append(i.split(' '))

for item in instructions:
    print(f'verb: {item[0]}, distance: {item[1]}')


#show_grid()
head_coords = {'y':OFFSET,'x':OFFSET}
tail_coords = {'y':OFFSET,'x':OFFSET}
grid[head_coords['y']][head_coords['x']] = 'H'
#show_grid()

# #head_coords = move_head(head_coords, ['R', '1'])
# move_head(['R', '3'])
# show_grid()
# move_head(['U', '3'])
# show_grid()
# move_head(['L', '2'])
# show_grid()
# move_head(['D', '2'])
# show_grid()
# move_head(['U', '3'])
# show_grid()
# move_head(['R', '4'])

print(f"head: {head_coords}")
print(f"tail: {tail_coords}")

for item in instructions:
    move_head(item)
    #show_grid()
    print(f"head: {head_coords}")
    print(f"tail: {tail_coords}")

grid.reverse()
#show_grid()
print(f"head: {head_coords}")
print(f"tail: {tail_coords}")

x_counter = 0
for row in grid:
    for item in row:
        if item == 'x' or item == 'T':
            x_counter += 1

print(f'tail locations: {x_counter}')

for item in tail_moves:
    print(item)

#show_grid()
uniq_locations = set(tail_moves)
print(tail_moves)
print(uniq_locations)
print(f'unique locations: {len(uniq_locations)}')
print(f'tail locations: {x_counter}')

show_grid()