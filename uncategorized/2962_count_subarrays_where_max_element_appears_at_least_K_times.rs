impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {

        let mut mx:i32 = 0;

        for num in nums.iter() {
            if num > &mx {
                mx = *num;
            }
        };

        let mut count:i32 = 0;
        let mut start:usize = 0;
        let mut ans:usize = 0;

        for end in 0.. nums.len() {

            if nums[end] == mx {
                count += 1;
            }

            while count >= k && start <= end {
                ans += nums.len() - end;
                if nums[start] == mx {
                    count -= 1;
                }
                start += 1;
            }

        };

        ans as i64

    }
}