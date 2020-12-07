f = open('input.txt', 'r')

total_sum = 0
char_count = {}
group_size = 0

for line in f:

  if line == '\n':
    for c in char_count:
      if char_count[c] == group_size:
        total_sum += 1

    char_count = {}
    group_size = 0

  else: 
    line = line.strip()
    group_size += 1
    for c in line:
      if c in char_count:
        char_count[c] = char_count[c] + 1
      else:
        char_count[c] = 1

print(total_sum)