''' split strings and find unique characters '''

from string import ascii_lowercase, ascii_uppercase
#INPUT_FILE = 'test.txt'
INPUT_FILE = 'real_input.txt'

priority_hash = {k: v for v, k in enumerate(ascii_lowercase, start=1)}
priority_hash |= {k: v for v, k in enumerate(ascii_uppercase, start=27)}


prio_sum = 0
group_count = 0
with open(INPUT_FILE, 'rt') as in_file:
    temp_list = []
    for line in in_file:
        group_count += 1
        temp_list.append(set(char for char in line.strip()))
        if group_count == 3:
            group_count = 0
            prio_sum += priority_hash[''.join(temp_list[0] & temp_list[1] & temp_list[2])]
            temp_list = []

print(f"Final sum: {prio_sum}")
