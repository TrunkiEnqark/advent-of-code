with open("input/.inp", "r") as file:
    rules, updates = file.read().split("\n\n", 1)
    
rules = [list(map(int, line.split('|'))) for line in rules.split('\n')]
updates = [list(map(int, line.split(','))) for line in updates.split('\n')]

def check_order(update, order_rules) -> bool:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in order_rules.get(update[j], set()):
                return False
    return True

def sort(update, order_rules) -> list[int]:
    for i in range(len(update)):
        idx = i
        for j in range(i + 1, len(update)):
            if update[idx] in order_rules.get(update[j], set()):
                update[idx], update[j] = update[j], update[idx]
    return update
    
order_rules = {}
for rule in rules:
    if rule[0] not in order_rules:
        order_rules[rule[0]] = set()
    order_rules[rule[0]].add(rule[1])    
    
result = 0
for update in updates:
    if not check_order(update, order_rules):
        new_update = sort(update, order_rules)
        print(new_update)
        result += new_update[len(update) // 2]

print(result)