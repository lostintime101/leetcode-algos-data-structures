use std::collections::HashMap;

impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {

        let mut ans:Vec<i32> = [0,0].to_vec();
        let mut freq:HashMap<i32, i32> = HashMap::new();

        for num in nums.iter() {
            let count = freq.entry(*num).or_insert(0);
            *count += 1;
        }

        for i in 1 ..nums.len() as i32 +1 {

            let count = freq.entry(i).or_insert(0);

            if *count == 0 {
                ans[1] = i;
            }
            if *count == 2 {
                ans[0] = i;
            }
        }

        ans

    }
}