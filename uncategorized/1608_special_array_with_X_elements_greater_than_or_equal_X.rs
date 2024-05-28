impl Solution {
    pub fn special_array(mut nums: Vec<i32>) -> i32 {

        nums.sort();
        nums.reverse();

        if *nums.last().unwrap() >= nums.len() as i32 {
            return nums.len() as i32;
        }

        for i in 0.. nums.len() -1 {
            if nums[i] >= (i+1) as i32 && nums[i+1] < (i+1) as i32 {
                return (i+1) as i32;
            }
        }

        -1
    }
}