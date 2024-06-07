use std::collections::HashMap;

impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {

        let mut d:HashMap<String, bool> = HashMap::new();

        for word in dictionary.iter() {
            d.insert(word.to_string(), true);
        }

        // println!("{:?}", d);

        let mut ans:Vec<String> = vec![];
        let words: Vec<&str> = sentence.split_whitespace().collect();

        for word in words {

            let mut new_word = String::new();
            let mut found = false;

            for (i, _) in word.chars().enumerate() {

                new_word = word[0..i+1].to_string();

                if d.contains_key(&new_word) {
                    ans.push(new_word);
                    found = true;
                    break;
                }
            }

            if !found {
                ans.push(word.to_string());
            }
        }

        ans.join(" ")

    }
}