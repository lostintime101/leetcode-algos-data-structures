impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {

        let mut ans:i32 = 0;
        let mut a_count:i32 = 0;

        for l in s.chars() {
            if l == 'a' {
                a_count += 1;
            }
        }

        ans = a_count;
        let mut b_front:i32 = 0;

        for l in s.chars() {
            if l == 'a' {
                a_count -= 1;
            } else {
                b_front += 1;
            }

            ans = i32::min(ans, a_count + b_front);
        }

        ans

    }
}