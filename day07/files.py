
from file_size import File, Directory

INPUT = 'test.txt'

with open(INPUT, 'rt') as infile:
    contents = infile.readlines()

cli_output = [line.split() for line in [entry.strip() for entry in contents]]

work_dir = ''
journal = {'/':Directory('/')}
for line in cli_output:
    if line[0] == '$':
        #print("I'm a command")
        if line[1] == 'cd':
            #print("change dir")
            if line[2] == '/':
                work_dir = '/'
                my_fs = Directory(work_dir)
            elif line[2] == '..':
                work_dir = work_dir[:-2]
            else:
                work_dir = work_dir + line[2] + '/'
                #my_fs.add_items(Directory(work_dir))
                #my_fs.contents[work_dir].add_items(Directory(work_dir))
            journal[work_dir] = Directory(work_dir) 

        #if line[1] == 'ls':
            #print("list dir")
            # collect output into current directory
    elif line[0] == 'dir':
        my_fs.add_items(Directory(work_dir))
        #pass 
    else:
        # collect output into current directory
        journal[work_dir].add_items(File(line[1],int(line[0])))
        if work_dir == '/':
            my_fs.add_items(File(line[1],int(line[0]))) 
        else:
            if work_dir not in my_fs.contents.keys():
                my_fs.add_items(Directory(work_dir))
            my_fs.contents[work_dir].add_items(File(line[1],int(line[0]))) 
