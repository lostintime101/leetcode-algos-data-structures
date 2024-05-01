impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {

        for(i,v) in word.chars().enumerate() {

            if v == ch {
                let (left,right) = word.split_at(i+1);
                let reversed_left = left.chars().rev().collect::<String>();
                return reversed_left + right;
            }
        }

        word

    }
}