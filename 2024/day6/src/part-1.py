grid = []
guard = (-1, -1)
with open("input/in.txt", "r") as file:
    for i, line in enumerate(file.read().split('\n')):
        grid.append(line.strip())
        if '^' in line.strip():
            guard = (i, line.strip().find('^'))

DIRECTIONS = [
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
]

n = len(grid)
visited = [[False for _ in range(n)] for _ in range(n)]

def check_range(i: int, j: int) -> bool:
    return 0 <= i < n and 0 <= j < n

def simulate_guard(i: int, j: int, k: int):
    direction = k
    while check_range(i, j):
        visited[i][j] = True
        ni, nj = i + DIRECTIONS[direction][0], j + DIRECTIONS[direction][1]
        if check_range(ni, nj) and grid[ni][nj] == '#':
            direction = (direction + 1) % 4
        else:
            i, j = ni, nj

simulate_guard(guard[0], guard[1], 0)    

result = sum(visited[i][j] for i in range(n) for j in range(n))
            
print(result)
