
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
        print("I'm a command")
        if line[1] == 'cd':
            print("change dir")
            if line[2] == '/':
                print("i'm root")
                print(f"work_dir={work_dir}")
                work_dir.append('/')
                journal[''.join(work_dir)] = Directory(work_dir)
                #root_dir = Directory(work_dir)
            elif line[2] == '..':
                print(f"work_dir before backout: {work_dir} type: {type(work_dir)}")
                work_dir = work_dir[:-2]
                print("backing out a dir")
                print(f"work_dir={work_dir}")
            else:
                #work_dir.append(line[2])
                #work_dir.append('/')
                test_key = ''.join(work_dir) + line[2] + '/'
                if test_key not in journal.keys():
                    print(f"adding {test_key}")
                    journal[test_key] = Directory(test_key)
                    journal[''.join(work_dir)].add(journal[test_key])
                ###work_dir = test_key
                work_dir.append(line[2])
                work_dir.append('/')
                print(f"moved into {line[2]}")
                print(f"work_dir: {work_dir}")
                #my_fs.add_items(Directory(work_dir))
                #my_fs.contents[work_dir].add_items(Directory(work_dir))
                #journal[''.join(work_dir)].add(Directory(''.join(work_dir))) 

        #if line[1] == 'ls':
            #print("list dir")
            # collect output into current directory
    elif line[0] == 'dir':
        #my_fs.add(Directory(''.join(work_dir)))
        print(f"need to add directory {line[1]}")
        test_key = ''.join(work_dir) + line[1] + '/'
        if test_key not in journal.keys():
            print(f"adding dir: {test_key}")
            journal[test_key] = Directory(test_key)
            journal[''.join(work_dir)].add(journal[test_key])
        #journal[''.join(work_dir)].add(Directory(''.join(work_dir + [line[1]])))
        #pass 
    else:
        #if work_dir == '/':
        #    print(f"add file {line[1]} while in {work_dir}")
        #    my_fs.add(File(line[1],int(line[0]))) 
        #else:
        print(f"add file {line[1]} of size {line[0]} while in {''.join(work_dir)}")
        journal[''.join(work_dir)].add(File(line[1],int(line[0])))
        # collect output into current directory
        #journal[''.join(work_dir)].add(File(line[1],int(line[0])))
        #if work_dir == '/':
            #print(f"add file {line[1]} while in {work_dir}")
            #my_fs.add(File(line[1],int(line[0]))) 
        #else:
           # print(f"add file {line[1]} of size {line[0]} while in {''.join(work_dir)}")
            #journal[''.join(work_dir)].add(File(line[1],int(line[0])))
            #if ''.join(work_dir) not in my_fs.children:
                #my_fs.add(Directory(''.join(work_dir)))
            #my_fs.children[''.join(work_dir)].add(File(line[1],int(line[0]))) 

journal['/'].operation()
dirs_total = 0
for i in journal:
    if journal[i].file_size <= 100000:
        dirs_total += journal[i].file_size
print(dirs_total)
