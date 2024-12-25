use std::collections::HashMap;

const INPUT: &str = include_str!("../input/in.txt");

#[derive(Clone, Copy)]
enum Operation {
    Add,
    Mul,
    Concat,
}

fn concat(a: u64, b: u64) -> u64 {
    (a.to_string() + &b.to_string()).parse().unwrap()
}

fn calc(a: u64, b: u64, operator: Operation) -> u64 {
    match operator {
        Operation::Add => a + b,
        Operation::Mul => a * b,
        Operation::Concat => concat(a, b)
    }
}

fn is_valid(target: u64, curr: u64, values: &[u64], operations: &[Operation]) -> bool {
    if values.is_empty() {
        return curr == target;
    }

    if curr > target {
        return false;
    }

    operations.iter().any(|&op| {
        is_valid(
            target,
            calc(curr, values[0], op),
            &values[1..],
            operations
        )
    })
}

fn result(map: &[(u64, Vec<u64>)], operations: &[Operation]) -> u64 {
    map.into_iter()
        .filter(|(key, values)| is_valid(*key, values[0], &values[1..], operations))
        .map(|(key, _)| key)
        .sum()
}

fn main() {
    let mut map: Vec<(u64, Vec<u64>)> = Vec::new();
    let mut lines_count = 0;
    for line in INPUT.lines() {
        let parts: Vec<&str> = line.split(":").collect();
        if parts.len() == 2 {
            let key: u64 = parts[0].trim().parse().unwrap();
            let values: Vec<u64> = parts[1]
                .split_whitespace()
                .map(|v| v.parse().unwrap())
                .collect();
            map.push((key, values));  // corrected line
        }
        lines_count += 1;
    }

    println!("Total lines: {}", lines_count);
    println!("Map length after read: {}", map.len());
    println!("Result (part 1): {}", result(&map, &[Operation::Add, Operation::Mul]));
    println!("Result (part 2): {}", result(&map, &[Operation::Add, Operation::Mul, Operation::Concat])); 
}
