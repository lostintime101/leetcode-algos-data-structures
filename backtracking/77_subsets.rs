impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {

        let mut ans: Vec<Vec<i32>> = Vec::new();

        pub fn generate(curr: Vec<i32>, i:usize, nums: &Vec<i32>, ans: &mut Vec<Vec<i32>>) {

            if i == nums.len() {
                ans.push(curr);
                return ;
            }

            let mut new_curr = curr.clone();
            new_curr.push(nums[i]);

            generate(curr, i+1, nums, ans);
            generate(new_curr, i+1, nums, ans);
        }

        generate(vec![], 0, &nums, &mut ans);

        ans

    }
}