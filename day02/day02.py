with open('day02-input', 'rt') as file:
    contents = file.read()

rounds = contents.split('\n')

def calculate_match(match):
    if match[0] == 'A':
        if match[1] == 'X':
            # rock(1) draws(3) rock
            return 1 + 3
        if match[1] == 'Y':
            # paper(2) beats(6) rock
            return 2 + 6
        if match[1] == 'Z':
            # scissors(3) losses(0) to rock
            return 3 + 0
    if match[0] == 'B':
        if match[1] == 'X':
            # rock(1) loses(0) to paper 
            return 1 + 0
        if match[1] == 'Y':
            # paper(2) draws(3) paper
            return 2 + 3
        if match[1] == 'Z':
            # scissors(3) beats(6) paper
            return 3 + 6
    if match[0] == 'C':
        if match[1] == 'X':
            # rock(1) beats(6) scissors
            return 1 + 6
        if match[1] == 'Y':
            # paper(2) loses(0) to scissors
            return 2 + 0
        if match[1] == 'Z':
            # scissors(3) draws(3) to scissors
            return 3 + 3

total = 0
for round in rounds:
    if round: 
        total += calculate_match(round.split())

print(total)
