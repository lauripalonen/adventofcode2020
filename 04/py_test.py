import re

test_string = "123cm"

splitted = re.split('(\d+)', test_string)
print(splitted)
