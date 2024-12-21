import re

with open('input/.inp', 'r') as file:
    content = file.read()
    
pattern = r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)'

matches = re.findall(pattern, content)

result = 0
enable = True

for match in matches:
    # print(match)
    if match == 'do()':
        enable = True
    elif match == "don't()":
        enable = False
    elif enable and "mul" in match:
        values = re.findall(r'\d+', match)
        result += int(values[0]) * int(values[1])
    
print(result) 