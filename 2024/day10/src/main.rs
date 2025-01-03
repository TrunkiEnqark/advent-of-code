use std::collections::HashSet;

const INPUT: &str = include_str!("../input/in.txt");
const DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (0, -1), (1, 0), (0, 1)];

fn get_start_points(grid: Vec<Vec<usize>>) -> Vec<(usize, usize)> {
    let mut start_points: Vec<(usize, usize)> = Vec::new();
    for (row_index, rows) in grid.iter().enumerate() {
        for (col_index, element) in rows.iter().enumerate() {
            if *element == 0 as usize {
                start_points.push((row_index, col_index));
            }
        }
    }
    start_points
}

fn in_bound(i: i32, j: i32, n: i32, m: i32) -> bool {
    i >= 0 && i < n && j >= 0 && j < m
}

fn count_reachable(grid: Vec<Vec<usize>>, point: (usize, usize)) -> usize {
    let mut stack = Vec::new();
    let mut reachable_points = HashSet::new();
    
    stack.push(point);

    while let Some((i, j)) = stack.pop() {
        if grid[i][j] == 9 {
            reachable_points.insert((i, j));
            continue;
        }

        for (dx, dy) in DIRECTIONS {
            let (ni, nj)= (i as i32 + dx, j as i32 + dy);
            
            if in_bound(ni, nj, grid.len() as i32, grid[0].len() as i32) {
                if grid[ni as usize][nj as usize] == grid[i][j] + 1 {
                    stack.push((ni as usize, nj as usize));
                }
            }
        }
    }

    reachable_points.len()
}

fn count_distinct_reachable(grid: Vec<Vec<usize>>, point: (usize, usize)) -> usize {
    let mut stack = Vec::new();
    let mut reachable_points: usize = 0;
    
    stack.push(point);

    while let Some((i, j)) = stack.pop() {
        if grid[i][j] == 9 {
            reachable_points += 1;
            continue;
        }

        for (dx, dy) in DIRECTIONS {
            let (ni, nj)= (i as i32 + dx, j as i32 + dy);
            
            if in_bound(ni, nj, grid.len() as i32, grid[0].len() as i32) {
                if grid[ni as usize][nj as usize] == grid[i][j] + 1 {
                    stack.push((ni as usize, nj as usize));
                }
            }
        }
    }

    reachable_points
}

fn scores_trailheads(grid: Vec<Vec<usize>>, start_points: Vec<(usize, usize)>) -> usize {
    let mut result = 0;
    for point in &start_points {
        result += count_reachable(grid.clone(), *point);
    }
    result
}

fn scores_distinct_trailheads(grid: Vec<Vec<usize>>, start_points: Vec<(usize, usize)>) -> usize {
    let mut result = 0;
    for point in &start_points {
        result += count_distinct_reachable(grid.clone(), *point);
    }
    result
}

fn main() {
    let grid = INPUT
        .lines()
        .map(|x| {
            x.chars()
                .map(|ch| {
                    ch.to_digit(10).unwrap() as usize
                })
                .collect::<Vec<_>>()
            }
        )
        .collect::<Vec<Vec<usize>>>();

    let start_points = get_start_points(grid.clone());

    println!("{}", scores_trailheads(grid.clone(), start_points.clone()));
    println!("{}", scores_distinct_trailheads(grid.clone(), start_points.clone()));
}
