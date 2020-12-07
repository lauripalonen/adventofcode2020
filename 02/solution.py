f = open("input.txt", "r")

input_data = []

for line in f:
  splitted = line.strip().split(' ')
  
  nums = splitted[0].split('-')
  min_val = int(nums[0])
  max_val = int(nums[1])

  letter = splitted[1][0]

  password = splitted[2]

  input_data.append({'min_val': min_val, 'max_val': max_val, 'letter': letter, 'pw': password})

valid_pws = 0

for entry in input_data:
  letter = entry['letter']
  pw = entry['pw']

  letter_count = 0

  for l in pw:
    if l == letter:
      letter_count += 1

  if letter_count >= entry['min_val'] and letter_count <= entry['max_val']:
    valid_pws += 1

print(valid_pws)
