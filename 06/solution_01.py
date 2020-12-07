f = open('input.txt', 'r')

total_sum = 0
group_answers = set()

for line in f:
  
  if line == '\n':
    total_sum += len(group_answers)
    group_answers.clear()

  else:
    line = line.strip()
    for c in line:
      group_answers.add(c)

print(total_sum)