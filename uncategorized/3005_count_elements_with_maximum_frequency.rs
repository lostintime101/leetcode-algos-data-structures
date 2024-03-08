use std::collections::HashMap;

impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {

        let mut ans:i32 = 0;
        let mut mx:i32 = 0;
        let mut counts:HashMap<i32, i32> = HashMap::new();

        for num in nums.iter() {
            let count = counts.entry(*num).or_insert(0);
            *count += 1;
            mx = i32::max(mx, *count);
        }

        for (i,v) in counts.iter() {
            if *v == mx {
                ans += v;
            }
        }

        ans

    }
}