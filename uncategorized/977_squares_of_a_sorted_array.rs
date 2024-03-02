impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {

        let mut ans = nums.clone();

        for (i,num) in nums.iter().enumerate() {
            ans[i] = num * num;
        }
        ans.sort();
        ans
    }
}