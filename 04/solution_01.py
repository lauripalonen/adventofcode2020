import re
f = open('input.txt', 'r')

input_data = []

def validate(data):
  if data[0] == 'byr':
    byr = int(data[1])
    if byr < 1920 or byr > 2002:
      return False

  if data[0] == 'iyr':
    iyr = int(data[1])
    if iyr < 2010 or iyr > 2020:
      return False

  if data[0] == 'eyr':
    eyr = int(data[1])
    if eyr < 2020 or eyr > 2030:
      return False

  if data[0] == 'hgt':
    hgt_unit_pair = re.split(r'(\d+)', data[1])[1:3]
    if len(hgt_unit_pair) != 2:
      return False

    unit = hgt_unit_pair[1]
    hgt = int(hgt_unit_pair[0])

    if unit == 'cm':
      if hgt < 150 or hgt > 193:
        return False
    
    elif unit == 'in':
      if hgt < 59 or hgt > 76:
        return False

    else:
      return False

  if data[0] == 'hcl':
    if data[1][0] != '#':
      return False
    
    value = data[1][1:len(data[1])]

    if len(value) != 6 or not value.isalnum():
      return False

  if data[0] == 'ecl':
    if not re.fullmatch('amb|blu|brn|gry|grn|hzl|oth', data[1]):
      return False

  if data[0] == 'pid':
    if len(data[1]) != 9 or not data[1].isdigit():
      return False

  return True

def parse_line(line):
  line = line.strip()
  items = line.split(' ')
  field_value_pairs = []

  for i in items:
    data = i.split(':')
    if len(data) == 2:
      if validate(data): 
        field_value_pairs.append(data)

  return field_value_pairs


passport = {}

for line in f:
  if not line.strip():
    input_data.append(passport)
    passport = {}

  field_value_pairs = parse_line(line)

  for p in field_value_pairs:
    passport[p[0]] = p[1]

valid_pp = 0

for p in input_data:
  if len(p) == 8 or (len(p) == 7 and not 'cid' in p):
    valid_pp += 1

print(valid_pp)







  

