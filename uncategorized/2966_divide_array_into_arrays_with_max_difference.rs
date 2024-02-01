impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {

        let mut nums = nums;
        nums.sort_unstable();

        let mut ans:Vec<Vec<i32>> = Vec::new();
        let mut curr:Vec<i32> = Vec::new();

        if (nums.len() % 3) != 0 {
            return ans;
        }

        for i in 0.. nums.len() {

            curr.push(nums[i]);

            if i % 3 == 2 {

                if (curr.last().unwrap() - curr.first().unwrap()) > k {
                    return vec![];
                }

                ans.push(curr.clone());
                curr.clear();
            }
        }

        ans

    }
}