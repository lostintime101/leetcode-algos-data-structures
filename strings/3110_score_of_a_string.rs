impl Solution {
    pub fn score_of_string(s: String) -> i32 {

        let mut ans: i32 = 0;
        let bytes = s.as_bytes();

        for i in 0.. (bytes.len() -1) {

            ans += (bytes[i] as i32 - bytes[i+1] as i32).abs();
        }

        ans

    }
}