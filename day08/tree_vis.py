#with open('test_grid.txt', 'rt') as in_file:
with open('puzzle_grid.txt', 'rt') as in_file:
    contents = in_file.read().strip()

lines = contents.split()

max_x = len(lines[0])
max_y = len(lines)

vis_lines = []
for i in lines:
    vis_lines.append([[int(char), False] for char in i])


def check_up(x, y):
    if vis_lines[y][x][1] == True:
        return True
    for i in range(y):
        if vis_lines[i][x][0] >= vis_lines[y][x][0]:
            return False
    return True


def check_down(x, y):
    if vis_lines[y][x][1] == True:
        return True
    for i in range(max_y - 1, y, -1):
        if vis_lines[i][x][0] >= vis_lines[y][x][0]:
            return False
    return True


def check_left(x, y):
    if vis_lines[y][x][1] == True:
        return True

    for i in range(x):
        if vis_lines[y][i][0] >= vis_lines[y][x][0]:
            return False
    return True


def check_right(x, y):
    if vis_lines[y][x][1] == True:
        return True

    for i in range(max_x - 1, x, -1):
        if vis_lines[y][i][0] >= vis_lines[y][x][0]:
            return False
    return True


for x in range(max_x):
    for y in range(max_y):
        vis_lines[y][x][1] = check_left(x, y)
        vis_lines[y][x][1] = check_right(x, y)
        vis_lines[y][x][1] = check_up(x, y)
        vis_lines[y][x][1] = check_down(x, y)

true_count = 0
for line in vis_lines:
    for entry in line:
        if entry[1]:
            true_count += 1

print(f'true_count: {true_count}')
