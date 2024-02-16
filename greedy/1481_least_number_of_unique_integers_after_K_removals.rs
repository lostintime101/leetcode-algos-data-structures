use std::collections::HashMap;

impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {

        let mut freq:HashMap<i32, i32> = HashMap::new();

        for a in arr {
            freq
                .entry(a)
                .and_modify(|c| *c += 1)
                .or_insert(1);
        }

        let mut counts: Vec<i32> = Vec::new();

        for (i,v) in freq.iter(){
            counts.push(*v);
        }

        counts.sort_unstable();

        let mut remove:i32 = 0;
        let mut k = k;

        for count in counts.iter() {
            if *count <= k {
                remove += 1;
                k -= count;
            } else {
                break;
            }
        }

        counts.len() as i32 - remove
    }
}