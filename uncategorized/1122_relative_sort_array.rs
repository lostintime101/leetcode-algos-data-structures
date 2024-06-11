use std::collections::HashMap;

impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {

        let mut ans:Vec<i32> = Vec::new();
        let mut count:HashMap<i32, i32> = HashMap::new();

        for v in arr1.iter() {
            let mut c = count.entry(*v).or_insert(0);
            *c += 1;
        }

        for v in arr2.iter() {
            let c = count[v];
            for _ in 0..c {
                ans.push(*v);
            }
            count.remove(v);
        }

        let mut end:Vec<i32> = Vec::new();

        for (k,v) in count {
            for _ in 0.. v {
                end.push(k);
            }
        }

        end.sort();
        ans.extend(end);

        ans

    }
}