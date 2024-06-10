impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {

        let mut sorted_heights = heights.clone();
        sorted_heights.sort();

        let mut ans = 0;

        for i in 0.. heights.len() {
            if sorted_heights[i] != heights[i] {
                ans += 1;
            }
        }

        ans

    }
}