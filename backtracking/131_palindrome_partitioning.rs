impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {

        let mut ans: Vec<Vec<String>> = Vec::new();
        let mut curr: Vec<String> = Vec::new();

        fn generate(
            curr: &mut Vec<String>,
            start: usize,
            end: usize,
            ans: &mut Vec<Vec<String>>,
            s: &str
        ) {
            if end > s.len() {
                return;
            }

            if s[start..end] == s[start..end].chars().rev().collect::<String>() {

                curr.push(s[start..end].to_string());

                if end == s.len() {
                    ans.push(curr.clone());
                } else {
                    generate(curr, end, end+1, ans, s);
                }

                curr.pop();
            }

            generate(curr, start, end+1, ans, s);
        }

        generate(&mut curr, 0, 1, &mut ans, &s);

        ans
    }
}