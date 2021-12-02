# process
with open('inputs/2.txt') as f:
    lines = f.readlines()
    data = [[line.split(' ')[0], int(line.split(' ')[1].strip())] for line in lines]


# part 1
horizontal = 0
vertical = 0
for tup in data:
  if tup[0] == 'forward':
    horizontal += tup[1]
  elif tup[0] == 'up':
    vertical -= tup[1]
  elif tup[0] == 'down':
    vertical += tup[1]
print('part 1:', horizontal * vertical)

## part 2
horizontal = 0
vertical = 0
aim = 0
for tup in data:
  if tup[0] == 'forward':
    horizontal += tup[1]
    vertical += aim * tup[1]
  elif tup[0] == 'up':
    aim -= tup[1]
  elif tup[0] == 'down':
    aim += tup[1]
print('part 2:', horizontal * vertical)
