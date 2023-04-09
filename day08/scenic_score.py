import math

#with open('test_grid.txt', 'rt') as in_file:
with open('puzzle_grid.txt', 'rt') as in_file:
    raw_contents = in_file.read().strip()

contents = []
for line in raw_contents.split():
    contents.append([[int(item), []] for item in line])

max_x = len(contents[0])
max_y = len(contents)


def check_up(x, y):

    raw_value = contents[y][x][0]

    # literal edge case
    if y == 0:
        contents[y][x][1].append(0)
        return None

    # loop through calculating the distance looking "up"
    # this is confusing since the y axis feels inverted
    next_tree_distance = 0
    for i in range(y - 1, -1, -1):
        if contents[i][x][0] >= raw_value:
            next_tree_distance += 1
            contents[y][x][1].append(next_tree_distance)
            return None
        next_tree_distance += 1
    #next_tree_distance += 1
    contents[y][x][1].append(next_tree_distance)
    #print(f'{x}, {y} - next_tree: {next_tree_distance}')
    return None


def check_left(x, y):
    raw_value = contents[y][x][0]

    # literal edge case
    if x == 0:
        contents[y][x][1].append(0)
        return None

    next_tree_distance = 0
    for i in range(x - 1, -1, -1):
        if contents[y][i][0] >= raw_value:
            next_tree_distance += 1
            contents[y][x][1].append(next_tree_distance)
            return None
        next_tree_distance += 1
    contents[y][x][1].append(next_tree_distance)


def check_right(x, y):
    raw_value = contents[y][x][0]

    # literal edge case
    if x == max_x - 1:
        contents[y][x][1].append(0)
        return None

    next_tree_distance = 0
    for i in range(x + 1, max_x):
        if contents[y][i][0] >= raw_value:
            next_tree_distance += 1
            contents[y][x][1].append(next_tree_distance)
            return None
        next_tree_distance += 1
    contents[y][x][1].append(next_tree_distance)


def check_down(x, y):
    raw_value = contents[y][x][0]

    # literal edge case
    if y == max_y - 1:
        contents[y][x][1].append(0)
        return None

    # loop through calculating the distance looking "down"
    # this is confusing since the y axis feels inverted
    next_tree_distance = 0
    for i in range(y + 1, max_y):
        if contents[i][x][0] >= raw_value:
            next_tree_distance += 1
            contents[y][x][1].append(next_tree_distance)
            return None
        next_tree_distance += 1
    #next_tree_distance += 1
    contents[y][x][1].append(next_tree_distance)
    #print(f'{x}, {y} - next_tree: {next_tree_distance}')
    return None


for line in contents:
    #print(line)
    pass

scores_list = []
for y in range(max_y):
    for x in range(max_x):
        check_up(x, y)
        check_left(x, y)
        check_right(x, y)
        check_down(x, y)
        #print(contents[y][x])
        scores_list.append(math.prod(contents[y][x][1]))

#print(contents)
scores_list.sort()
print(scores_list[-1])
