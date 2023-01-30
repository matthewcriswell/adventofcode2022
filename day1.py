with open('day1-input', 'rt') as file:
    contents = file.read().split('\n\n')

group_list = []
for single in contents:
    backpack = single.split()
    group_list.append(backpack)

max_val = 0
for item in group_list:
    my_sum = sum([int(nums) for nums in item])
    print(my_sum)
    if my_sum > max_val:
        max_val = my_sum

print(f'max: {max_val}')
