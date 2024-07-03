impl Solution {
    pub fn min_difference(mut nums: Vec<i32>) -> i32 {

        let poss = [[0, -4], [1, -3], [2, -2], [3, -1]];
        let mut ans:i32 = i32::MAX;
        nums.sort();

        if nums.len() <= 3 {
            return 0;
        }

        for [start, end] in poss.iter() {
            let curr = (nums[*end as usize + nums.len()] - nums[*start as usize]).abs();
            ans = i32::min(ans, curr);
        }

        ans

    }
}