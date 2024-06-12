impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {

        let mut curr:usize = 0;

        for v in 0.. 2 {

            for i in curr.. nums.len() {

                if nums[i] == v {
                    nums[i] = nums[curr];
                    nums[curr] = v;
                    curr += 1;
                }
            }
        }
    }
}