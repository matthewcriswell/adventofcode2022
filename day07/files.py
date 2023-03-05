from scratch import File, Directory

#INPUT = 'test.txt'
INPUT = 'input.txt'

with open(INPUT, 'rt') as infile:
    contents = infile.readlines()

cli_output = [line.split() for line in [entry.strip() for entry in contents]]

work_dir = []
journal = {}
for line in cli_output:
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                work_dir.append('/')
                journal[''.join(work_dir)] = Directory(work_dir)
            elif line[2] == '..':
                work_dir = work_dir[:-2]
            else:
                test_key = ''.join(work_dir) + line[2] + '/'
                if test_key not in journal.keys():
                    journal[test_key] = Directory(test_key)
                    journal[''.join(work_dir)].add(journal[test_key])
                work_dir.append(line[2])
                work_dir.append('/')
    elif line[0] == 'dir':
        test_key = ''.join(work_dir) + line[1] + '/'
        if test_key not in journal.keys():
            journal[test_key] = Directory(test_key)
            journal[''.join(work_dir)].add(journal[test_key])
    else:
        journal[''.join(work_dir)].add(File(line[1], int(line[0])))

journal['/'].operation()
dirs_total = 0
for i in journal:
    if journal[i].file_size <= 100000:
        dirs_total += journal[i].file_size
print(dirs_total)
