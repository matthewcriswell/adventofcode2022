''' find overlap in ranges of numbers '''

#INPUT = 'test.txt'
INPUT = 'input.txt'

overlaps = 0

with open(INPUT, 'rt') as infile:
    for line in infile:
        first_range = line.strip().split(',')[0].split('-')
        second_range = line.strip().split(',')[1].split('-')
        first_range = [int(item) for item in first_range]
        second_range = [int(item) for item in second_range]

        first_range_nums = []
        for i in range(first_range[0], first_range[1] + 1):
            first_range_nums.append(i)
        first_range_set = set(first_range_nums)

        second_range_nums = []
        for i in range(second_range[0], second_range[1] + 1):
            second_range_nums.append(i)
        second_range_set = set(second_range_nums)

        if first_range_set.issubset(
                second_range_set) or second_range_set.issubset(
                    first_range_set):
            overlaps += 1

print(f'overlaps: {overlaps}')
