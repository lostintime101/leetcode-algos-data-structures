impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {

        use core::cmp::max;

        nums.sort();
        let mut ans = 0;

        for i in 0.. (nums.len() / 2) {
            ans = max(ans, nums[i] + nums[nums.len() - (i+1)]);
        }

        ans
    }

}