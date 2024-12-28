const INPUT: &str = include_str!("../input/in.txt");

fn filesystem_checksum_p1(disk_map: &[usize]) -> usize {
    let mut disk_data: Vec<_> = vec![];
    let mut id = 0;

    for (i, length) in disk_map.iter().enumerate() {
        if i % 2 == 0 {
            for _ in 0..*length {
                disk_data.push((id, 1));
            }
            id += 1;
        } else {
            for _ in 0..*length {
                disk_data.push((id, 0));
            }
        }
    }

    while let Some(pos) = disk_data.iter().rposition(|&(_, block_type)| block_type == 1) {
        if let Some(free_pos) = disk_data.iter().position(|&(_, block_type)| block_type == 0) {
            if free_pos < pos {
                let temp = disk_data[free_pos];
                disk_data[free_pos] = disk_data[pos];
                disk_data[pos] = temp;
            } else {
                break;
            }
        } else {
            break;
        }
    }

    disk_data
        .iter()
        .enumerate()
        .filter(|&(_, (_, block_type))| *block_type == 1)
        .map(|(i, (id, _))| i * id)
        .sum()
}

fn block_checksum(id: usize, start: usize, length: usize) -> usize {
    id * (start * length + length * (length - 1) / 2)
}

fn filesystem_checksum_p2(disk_map: &mut [usize]) -> usize {
    let n = disk_map.len();
    let mut idx = vec![0; n];
    let mut result: usize = 0;

    for i in 1..n {
        idx[i] = idx[i - 1] + disk_map[i - 1];
    }

    for i in (0..n).step_by(2).rev() {
        let mut start = idx[i];
        for j in (1..i).step_by(2) {
            if disk_map[j] < disk_map[i] {
                continue;
            }

            start = idx[j];

            disk_map[j] -= disk_map[i];
            idx[j] += disk_map[i];
            break;
        }

        result += block_checksum(i / 2, start, disk_map[i]);
    }

    result
}

fn main() {
    let mut nums: Vec<_> = INPUT.trim().bytes().map(|x| (x - b'0') as usize).collect();
    println!("{}", filesystem_checksum_p1(&nums));
    println!("{}", filesystem_checksum_p2(&mut nums));
}