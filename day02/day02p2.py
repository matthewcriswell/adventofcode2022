#with open('day02-sample-input', 'rt') as file:
with open('day02-input', 'rt') as file:
    contents = file.read()

rounds = contents.split('\n')
def calculate_match(match):
    # opponent plays rock
    if match[0] == 'A':
        if match[1] == 'X':
            # lose(0) by playing scissors(3)
            return 0 + 3
        if match[1] == 'Y':
            # draw(3) by playing rock(1)
            return 3 + 1
        #else win(6) by playing paper(2)
        return 6 + 2
    # opponent plays paper
    if match[0] == 'B':
        if match[1] == 'X':
            # lose(0) by playing rock(1)
            return 0 + 1
        if match[1] == 'Y':
            # draw(3) by playing paper(2)
            return 3 + 2
        # else win(6) by playing scissors(3)
        return 6 + 3
    # opponent plays scissors
    if match[0] == 'C':
        if match[1] == 'X':
            # lose(0) by playing paper(2)
            return 0 + 2
        if match[1] == 'Y':
            # draw(3) by playing scissors(3)
            return 3 + 3 
        # else win(6) by playing rock(1)
        return 6 + 1

total = 0
for match in rounds:
    if match: 
        total += calculate_match(match.split())

print(total)
