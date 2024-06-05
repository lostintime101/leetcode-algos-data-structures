impl Solution {
    pub fn common_chars(words: Vec<String>) -> Vec<String> {

        let mut ans:Vec<String> = Vec::new();
        let mut prev: [u32;26] = [0; 26];

        for c in words[0].chars() {
            let l = (c as usize) - 'a' as usize;
            prev[l] += 1;
        }

        for i in 1.. words.len() {

            let mut curr: [u32;26] = [0; 26];
            for c in words[i].chars() {

                let l = c as usize - 'a' as usize;
                if prev[l] > 0 {
                    curr[l] += 1;
                    prev[l] -= 1;
                }
            }

            prev = curr;
        }

        for (mut i,v) in prev.iter().enumerate() {
            i += 97;
            for _ in 0.. *v {
                ans.push(String::from(char::from_u32(i as u32).unwrap()));
            }
        }

        ans

    }
}