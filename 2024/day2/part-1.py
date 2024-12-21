cnt = 0
with open('input.inp', 'r') as file:
    for line in file:
        ls = list(map(int, line.strip().split()))
        
        is_increasing = ls[1] - ls[0] > 0
        is_safe = True
        for i in range(len(ls) - 1):
            if abs(ls[i + 1] - ls[i]) == 0 or abs(ls[i + 1] - ls[i]) > 3:
                is_safe = False
                break
            if is_increasing and ls[i + 1] - ls[i] < 0:
                is_safe = False
                break
            if not is_increasing and ls[i + 1] - ls[i] > 0:
                is_safe = False
                break
        
        # print(is_safe)
        cnt += is_safe
print(cnt)