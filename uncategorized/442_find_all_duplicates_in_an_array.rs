impl Solution {
    pub fn find_duplicates(nums: Vec<i32>) -> Vec<i32> {

        let mut nums = nums;
        let mut ans:Vec<i32> = Vec::new();

        for i in 0.. nums.len() {
            let mut curr = nums[i];
            if curr < 0 {
                curr *= -1;
            }
            curr -= 1;
            if nums[curr as usize] < 0 {
                ans.push(curr + 1);
            } else {
                nums[curr as usize] *= -1;
            }
        };

        ans

    }
}