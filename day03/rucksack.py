''' split strings and find unique characters '''

from string import ascii_lowercase, ascii_uppercase
#INPUT_FILE = 'test.txt'
INPUT_FILE = 'real_input.txt'

priority_hash = {k: v for v, k in enumerate(ascii_lowercase, start=1)}
priority_hash |= {k: v for v, k in enumerate(ascii_uppercase, start=27)}

def find_uniq_prio(my_string):
    first_half = set(char for char in my_string[:int(len(my_string)/2)])
    second_half = set(char for char in my_string[int(len(my_string)/2):])
    return priority_hash[''.join(first_half & second_half)]

prio_sum = 0
with open(INPUT_FILE, 'rt') as in_file:
    for line in in_file:
        prio_sum += find_uniq_prio(line.strip())

print(f"Final sum: {prio_sum}")
