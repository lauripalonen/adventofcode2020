f = open('input.txt', 'r')

input_data = []

for line in f:
  row = []

  line = line.strip()

  for c in line:
    row.append(c)
  
  input_data.append(row)

def tree_counter(x_mov, y_mov):
  y = 0
  x = 0

  tree_count = 0

  while True:
    y += y_mov
    x += x_mov

    if y > len(input_data)-1:
      break

    if x > len(input_data[0])-1:
      x -= len(input_data[0])

    if input_data[y][x] == '#':
      tree_count += 1

  return tree_count

print(tree_counter(1, 1) * tree_counter(3, 1) * tree_counter(5, 1) * tree_counter(7, 1) * tree_counter(1, 2))