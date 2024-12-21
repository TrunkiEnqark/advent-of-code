def is_safe(ls: list[int]) -> bool:
    is_increasing = ls[1] - ls[0] > 0
    for i in range(len(ls) - 1):
        if abs(ls[i + 1] - ls[i]) == 0 or abs(ls[i + 1] - ls[i]) > 3:
            return False
        if is_increasing and ls[i + 1] - ls[i] < 0:
            return False
        if not is_increasing and ls[i + 1] - ls[i] > 0:
            return False
    return True

cnt = 0
with open('input.inp', 'r') as file:
    for line in file:
        ls = list(map(int, line.strip().split()))

        if is_safe(ls):
            cnt += 1
            continue
        
        for i in range(len(ls)):
            new_ls = ls[:i] + ls[i + 1 :]
            if is_safe(new_ls):
                cnt += 1
                break
print(cnt)