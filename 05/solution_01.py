import math

def iterate_rows(input):
  current_range = [0, 127]

  for c in input:

    if c == 'F':
      upper_value = math.floor((current_range[1] - current_range[0])/2)
      current_range = [current_range[0], current_range[0] + upper_value]

    if c == 'B':
      lower_value = math.ceil((current_range[1] - current_range[0])/2)
      current_range = [current_range[0] + lower_value, current_range[1]]

  return current_range[0] if input[6] == "F" else current_range[1]

def iterate_cols(input):
  current_range = [0, 7]

  for c in input:

    if c == "L":
      upper_value = math.floor((current_range[1] - current_range[0])/2)
      current_range = [current_range[0], current_range[0] + upper_value]

    if c == 'R':
      lower_value = math.ceil((current_range[1] - current_range[0])/2)
      current_range = [current_range[0] + lower_value, current_range[1]]

  return current_range[0] if input[2] == "L" else current_range[1]

def parse_pass(input):
  row = iterate_rows(input[0:7])
  col = iterate_cols(input[7:10])

  seat_id = row * 8 + col

  return {"seat_id": seat_id, "row": row, "col": col}

f = open('input.txt', 'r')

highest_id = -1

seat_array = [[0]*8 for i in range(128)]

taken_seats = 0
lines = 0

input_data = set()


for line in f:
  lines += 1
  line = line.strip()
  input_data.add(line)
  seat = parse_pass(line.strip())
  highest_id = max(highest_id, seat["seat_id"])

  row = seat["row"]
  col = seat["col"]

  if seat_array[row][col] == 0:
    seat_array[row][col] = seat["seat_id"]
  elif seat_array[row][col] == 1:
    taken_seats += 1

for i in range(len(seat_array)):
  print(seat_array[i])