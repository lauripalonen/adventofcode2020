f = open("input.txt", "r")

input_data = []

for line in f:
  splitted = line.strip().split(' ')
  
  nums = splitted[0].split('-')
  first_index = int(nums[0])
  second_index = int(nums[1])

  letter = splitted[1][0]

  password = splitted[2]

  input_data.append({'first_index': first_index, 'second_index': second_index, 'letter': letter, 'pw': password})

valid_pws = 0

for entry in input_data:
  letter = entry['letter']
  pw = entry['pw']

  letter_in_first_index = pw[entry['first_index']-1]
  letter_in_second_index = pw[entry['second_index']-1]

  if (letter_in_first_index == letter or letter_in_second_index == letter) and letter_in_first_index != letter_in_second_index:
    valid_pws += 1

print(valid_pws)
