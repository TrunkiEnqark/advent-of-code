with open("input/.inp", "r") as file:
    grid = [line.strip() for line in file]

def check(f: chr, s: chr) -> bool:
    return (f == 'M' and s == 'S') or (f == 'S' and s == 'M')

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i > 0 and i + 1 < len(grid) and j > 0 and j + 1 < len(grid[0]) and grid[i][j] == 'A':
            if check(grid[i-1][j-1], grid[i+1][j+1]) and check(grid[i-1][j+1], grid[i+1][j-1]):
                result += 1
            
print(result)
