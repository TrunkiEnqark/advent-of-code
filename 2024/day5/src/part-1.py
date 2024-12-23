with open("input/test.inp", "r") as file:
    rules, updates = file.read().split("\n\n", 1)
    
rules = [list(map(int, line.split('|'))) for line in rules.split('\n')]
updates = [list(map(int, line.split(','))) for line in updates.split('\n')]

def check_order(update, order_rules) -> bool:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in order_rules.get(update[j], set()):
                return False
    return True

order_rules = {}
for rule in rules:
    if rule[0] not in order_rules:
        order_rules[rule[0]] = set()
    order_rules[rule[0]].add(rule[1])    
    
result = 0
for update in updates:
    if not check_order(update, order_rules):
        print(update)
        result += update[len(update) // 2]

print(result)