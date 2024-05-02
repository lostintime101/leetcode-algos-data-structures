use std::collections::HashMap;

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {

        let mut possible:HashMap<i32,bool> = HashMap::new();

        for num in nums.iter() {
            let curr = possible.entry(*num).or_insert(false);
            *curr = true;
            let inverse_curr = possible.entry(*num * -1).or_insert(false);
        }

        let mut ans = -1;

        for num in nums.iter() {
            if possible[num] == true && possible[&(num * -1)] == true{
                ans = i32::max(ans, *num);
            }
        }

        // println!("{:?}", possible);
        ans

    }
}