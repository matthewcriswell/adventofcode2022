''' sort boxes based on input instructions '''

#INPUT = 'test.txt'
INPUT = 'input.txt'

#handle input
bort = 0
boxes = []
instructions = []

with open(INPUT, 'rt') as infile:
    contents = infile.read()

for line in contents.split('\n'):
    if len(line) == 0:
        bort += 1
    if bort == 0:
        boxes.append(line)
    if bort == 1:
        instructions.append(line)

# make box representation a little easier to work with
inverted_boxes = boxes[::-1]
columns = []
for entry in inverted_boxes[0]:
    if entry.isdigit():
        columns.append(inverted_boxes[0].find(entry))

# intialize dict of lists
box_redux = {}
for item in columns:
    item_key = inverted_boxes[0][item]
    box_redux[item_key] = []
for row in inverted_boxes[1:]:
    for item in columns:
        item_key = inverted_boxes[0][item]
        if row[item] != ' ':
            box_redux[item_key].append(row[item])
print(box_redux)


#instructions
if instructions[0] == '':
   instructions.pop(0)
   print("popped off a blank instruction")

for instruction in instructions:
   print(instruction.split())
   crates = int(instruction.split()[1])
   source_key = instruction.split()[3]
   dest_key = instruction.split()[5]
   print(f"move {crates} crates from {source_key} to {dest_key}")
   for i in range(crates):
       print(f"popping off {source_key}")
       payload = box_redux[source_key].pop()
       print(f"appending to {dest_key}")
       box_redux[dest_key].append(payload)

output = []
for entry in box_redux.values():
    output.append(entry[-1])

print(''.join(output))
