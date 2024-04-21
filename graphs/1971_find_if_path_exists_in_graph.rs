use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        let mut seen: Vec<bool> = vec![false; n as usize];
        let mut mapp: HashMap<i32, Vec<i32>> = HashMap::new();

        for edge in edges {
            let a = edge[0];
            let b = edge[1];
            let curr_a = mapp.entry(a).or_insert(Vec::new());
            curr_a.push(b);
            let curr_b = mapp.entry(b).or_insert(Vec::new());
            curr_b.push(a);
        }

        let mut prev = HashSet::new();
        prev.insert(source);
        let mut curr = HashSet::new();

        while !prev.is_empty() {
            for &p in &prev {
                if p == destination {
                    return true;
                }
                if seen[p as usize] {
                    continue;
                }
                seen[p as usize] = true;

                if let Some(routes) = mapp.get(&p) {
                    for &neighbor in routes {
                        curr.insert(neighbor);
                    }
                }
            }

            prev = std::mem::take(&mut curr);
        }

        false
    }
}
