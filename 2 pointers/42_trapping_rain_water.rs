impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {

        let N:usize = height.len();
        let mut big_l:Vec<i32> = vec![0; N];
        let mut big_r:Vec<i32> = vec![0; N];
        let mut ans:i32 = 0;

        let mut prev:i32 = 0;
        for i in 0.. N {
            big_l[i] = i32::max(height[i], prev);
            prev = big_l[i];
        }

        prev = 0;
        for i in (0.. N).rev() {
            big_r[i] = i32::max(height[i], prev);
            prev = big_r[i];
        }

        for i in 0.. N {
            ans += (i32::min(big_l[i], big_r[i]) - height[i]);
        }

        ans

    }
}