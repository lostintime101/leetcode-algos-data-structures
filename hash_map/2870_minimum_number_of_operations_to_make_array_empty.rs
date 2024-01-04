use std::collections::HashMap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {

        let mut ans:i32 = 0;
        let mut freq:HashMap<i32, i32> = HashMap::new();

        for num in nums {
            let mut count = freq.entry(num).or_insert(0);
            *count += 1;
        }

        for (k,v) in freq.iter() {
            if *v == 1 {
                return -1;
            }
            let curr:i32 = v % 3;
            ans += v / 3;
            if curr != 0 {
                ans += 1;
            }
        }

        ans

    }
}