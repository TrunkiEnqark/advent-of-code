with open("input/in.txt", "r") as f:
    stones = list(map(int, f.read().split(' ')))
    
from collections import Counter
from typing import Dict

def process_stone(stone: int) -> list[int]:
    stone_str = str(stone)
    
    if stone == 0:
        return [1]
    
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    
    return [stone * 2024]

def simulate_blinks_efficient(initial_stones: list[int], total_blinks: int) -> int:
    stone_counts = Counter(initial_stones)
    total_stones = len(initial_stones)
    
    for blink in range(total_blinks):
        new_stone_counts = Counter()
        
        for stone, count in stone_counts.items():
            new_stones = process_stone(stone)
            for new_stone in new_stones:
                new_stone_counts[new_stone] += count
        
        stone_counts = new_stone_counts
        total_stones = sum(stone_counts.values())
        
        print(f"Blink {blink + 1}/75, stones: {total_stones}")
    
    return total_stones

result = simulate_blinks_efficient(stones, 75)
print(f"{result}")