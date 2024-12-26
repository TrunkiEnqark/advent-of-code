use std::collections::{HashMap, HashSet};

const INPUT: &str = include_str!("../input/in.txt");

fn antinodes_count(positions: HashMap<char, Vec<(usize, usize)>>, n: usize, m: usize) -> usize {
   let mut antinodes: HashSet<(usize, usize)> = HashSet::new();

   for (_, positions) in positions.iter() {
       for i in 0..positions.len() {
           for j in 0..positions.len() {
               if i != j {
                   let (x1, y1) = positions[i];
                   let (x2, y2) = positions[j];
                   
                   let x3 = x1 as i32 * 2 - x2 as i32;
                   let y3 = y1 as i32 * 2 - y2 as i32;
                   
                   if x3 >= 0 && x3 < n as i32 && y3 >= 0 && y3 < m as i32 {
                       antinodes.insert((x3 as usize, y3 as usize));
                   }
               }
           }
       }
   }

   antinodes.len()
}

fn is_collinear(p1: (usize, usize), p2: (usize, usize), p3: (usize, usize)) -> bool {
    let (x1, y1) = (p1.0 as i32, p1.1 as i32);
    let (x2, y2) = (p2.0 as i32, p2.1 as i32);
    let (x3, y3) = (p3.0 as i32, p3.1 as i32);
    
    (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)
}

fn antinodes_part2_count(positions: HashMap<char, Vec<(usize, usize)>>, n: usize, m: usize) -> usize {
    let mut antinodes: HashSet<(usize, usize)> = HashSet::new();

    for (_, pos) in positions {
        for row in 0..n {
            for col in 0..m {
                let point = (row, col);
                let mut count = 0;

                for i in 0..pos.len() {
                    for j in (i+1)..pos.len() {
                        if is_collinear(pos[i], pos[j], point) {
                            count += 1;
                            break;
                        }
                    }
                }

                if count > 0 {
                    antinodes.insert(point);
                }
            }
        }
    }

    antinodes.len()
}

fn main() {
   let n: usize = INPUT.lines().count();
   let m: usize = INPUT.lines().next().unwrap().chars().count();

   let mut positions: HashMap<char, Vec<(usize, usize)>> = HashMap::new();

   for (row, line) in INPUT.lines().enumerate() {
       for (col, chr) in line.chars().enumerate() {
           if chr != '.' {
               positions.entry(chr)
                   .or_default()
                   .push((row, col));
           }
       }
   }

   println!("Part 1: {}", antinodes_count(positions.clone(), n, m));
   println!("Part 2: {}", antinodes_part2_count(positions.clone(), n, m));
}