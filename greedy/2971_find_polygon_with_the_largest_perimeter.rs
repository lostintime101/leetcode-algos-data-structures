impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i64 {

        let mut ans:i64 = -1;
        let mut nums = nums;
        nums.sort();

        let mut count: i64 = (nums[0] + nums[1]) as i64;

        for i in 2.. nums.len() {

            let curr = i64::from(nums[i]);

            if curr < count {
                count += curr;
                ans = count;
            } else {
                count += curr;
            }
        }

        ans

    }
}