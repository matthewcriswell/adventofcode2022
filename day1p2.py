with open('day1-input', 'rt') as file:
    contents = file.read().split('\n\n')

group_list = []
for single in contents:
    backpack = single.split()
    group_list.append(backpack)

backpack_list = []
max_val = 0
for item in group_list:
    my_sum = sum([int(nums) for nums in item])
    backpack_list.append(my_sum)

top_3_sum = sum(sorted(backpack_list, reverse=True)[:3])
print(f"Sum of top 3: {top_3_sum}")
