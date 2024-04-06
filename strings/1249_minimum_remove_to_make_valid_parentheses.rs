impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {

        let mut ends:i32 = 0;
        let mut opened:i32 = 0;
        let mut ans:String = String::new();

        for c in s.chars() {
            if c == ')' {
                ends += 1;
            }
        }

        for c in s.chars() {

            if c == '(' {
                if ends < 1 {
                    continue
                } else {
                    ends -= 1;
                    opened += 1;
                }
            }
            if c == ')' {
                if opened < 1 {
                    ends -= 1;
                    continue
                } else {
                    opened -= 1;
                }
            }

            ans.push(c);
        }

        ans

    }
}