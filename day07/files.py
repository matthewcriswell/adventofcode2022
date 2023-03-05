''' takes command line history as output and parses into a filesystem structure '''
from scratch import File, Directory

#INPUT = 'test.txt'
INPUT = 'input.txt'

with open(INPUT, 'rt', encoding='UTF-8') as infile:
    contents = infile.readlines()

cli_output = [line.split() for line in [entry.strip() for entry in contents]]

# keep track of current working dir
work_dir = []

# journal of directories
journal = {}

for line in cli_output:
    # check if command
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                work_dir.append('/')
                journal[''.join(work_dir)] = Directory(work_dir)
            elif line[2] == '..':
                work_dir = work_dir[:-2]
            else:
                test_key = ''.join(work_dir) + line[2] + '/'
                if test_key not in journal:
                    journal[test_key] = Directory(test_key)
                    journal[''.join(work_dir)].add(journal[test_key])
                work_dir.append(line[2])
                work_dir.append('/')
    # else check if line is a dir
    elif line[0] == 'dir':
        test_key = ''.join(work_dir) + line[1] + '/'
        if test_key not in journal:
            journal[test_key] = Directory(test_key)
            journal[''.join(work_dir)].add(journal[test_key])
    # else must be a file
    else:
        journal[''.join(work_dir)].add(File(line[1], int(line[0])))

free_space = 70000000 - journal['/'].get_size()
space_needed = 30000000 - free_space

dir_sizes = []
for i in journal:
    if journal[i].file_size > space_needed:
        dir_sizes.append(journal[i].file_size)
dir_sizes.sort()
print(dir_sizes[0])
