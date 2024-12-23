# Horizontal pattern
def get_pattern_1(grid: list[str], pattern: str, i: int, j: int) -> int:
    if j + 3 < len(grid[0]):
        p = grid[i][j : j+4]
        return int(p == pattern) + int(p == pattern[::-1])
    return 0

def get_pattern_2(grid: list[str], pattern: str, i: int, j: int) -> int:
    if i + 3 < len(grid):
        p = ''.join(grid[x][j] for x in range(i, i+4))
        return int(p == pattern) + int(p == pattern[::-1])
    return 0

def get_pattern_3(grid: list[str], pattern: str, i: int, j: int) -> int:
    if i + 3 < len(grid) and j + 3 < len(grid[0]):
        p = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
        return int(p == pattern) + int(p == pattern[::-1])
    return 0

def get_pattern_4(grid: list[str], pattern: str, i: int, j: int) -> int:
    if i + 3 < len(grid) and j - 3 >= 0:
        p = grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3]
        return int(p == pattern) + int(p == pattern[::-1])
    return 0

with open("input/.inp", "r") as file:
    grid = [line.strip() for line in file]

result = 0
PATTERN = "XMAS"

for i in range(len(grid)):
    for j in range(len(grid[0])):
        result += get_pattern_1(grid, PATTERN, i, j)
        result += get_pattern_2(grid, PATTERN, i, j)
        result += get_pattern_3(grid, PATTERN, i, j)
        result += get_pattern_4(grid, PATTERN, i, j)

print(result)
