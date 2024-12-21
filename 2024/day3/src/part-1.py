import re

with open('input/.inp', 'r') as file:
    content = file.read()
    
pattern = r'mul\(\d+,\d+\)'

matches = re.findall(pattern, content)

result = 0
enable = True

for match in matches:
    values = re.findall(r'\d+', match)
    result += int(values[0]) * int(values[1])
    
print(result) 