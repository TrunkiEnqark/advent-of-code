# wait for 55s :D

from collections import deque

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

def check_range(i: int, j: int) -> bool:
    return 0 <= i < n and 0 <= j < n

def is_loop(i: int, j: int, k: int, grid):
    visited = [[[False for _ in range(n)] for _ in range(n)] for _ in range(4)]
    direction = k
    queue = deque([(i, j, direction)])

    while queue:
        x, y, dir = queue.popleft()

        if visited[dir][x][y]:
            return True
        visited[dir][x][y] = True

        for _ in range(4):
            nx, ny = x + DIRECTIONS[dir][0], y + DIRECTIONS[dir][1]
            if check_range(nx, ny) and grid[nx][ny] == '#':
                dir = (dir + 1) % 4
            else:
                x, y = nx, ny
                break

        if not check_range(x, y):
            return False

        queue.append((x, y, dir))

    return False

result = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == '.':
            new_grid = [list(row) for row in grid]
            new_grid[i][j] = '#'
            if is_loop(guard[0], guard[1], 0, new_grid):
                result += 1

print(result)
