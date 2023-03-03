''' find signal marker '''
#INPUT = 'test.txt'
INPUT = 'input.txt'
with open(INPUT, 'rt') as infile:
    contents = infile.readlines()


def eval_string(my_string):
    my_list = [char for char in my_string]
    test_list = []
    for x, i in enumerate(my_list, 1):
        test_list.append(i)
        if len(set(test_list)) == 4:
            print(f'Sequence detected: {x}')
            break
        if x >= 4:
            test_list.pop(0)


for i in contents:
    eval_string(i.strip())
