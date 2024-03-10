use std::collections::HashMap;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {

        let mut ans:Vec<i32> = Vec::new();
        let mut count1:HashMap<i32, i32> = HashMap::new();

        for num in nums1.iter() {
            let count = count1.entry(*num).or_insert(0);
            *count += 1;
        };

        for num in nums2.iter() {
            let count = count1.entry(*num).or_insert(0);
            if *count > 0 {
                ans.push(*num);
                *count = 0;
            };
        };

        ans
    }
}