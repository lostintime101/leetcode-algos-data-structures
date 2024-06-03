
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_identical_strings() {
        let s = String::from("abc");
        let t = String::from("abc");
        assert_eq!(Solution::append_characters(s, t), 0);
    }

    #[test]
    fn test_t_is_substring_of_s() {
        let s = String::from("abcdef");
        let t = String::from("ace");
        assert_eq!(Solution::append_characters(s, t), 0);
    }

    #[test]
    fn test_t_not_present_in_s() {
        let s = String::from("abcdef");
        let t = String::from("xyz");
        assert_eq!(Solution::append_characters(s, t), 3);
    }

    #[test]
    fn test_empty_s() {
        let s = String::from("");
        let t = String::from("xyz");
        assert_eq!(Solution::append_characters(s, t), 3);
    }

    #[test]
    fn test_empty_t() {
        let s = String::from("abcdef");
        let t = String::from("");
        assert_eq!(Solution::append_characters(s, t), 0);
    }

    #[test]
    fn test_s_shorter_than_t_with_some_matching_characters() {
        let s = String::from("ace");
        let t = String::from("abcdef");
        assert_eq!(Solution::append_characters(s, t), 3);
    }

    #[test]
    fn test_s_longer_than_t_with_t_scattered_within_s() {
        let s = String::from("abacadaeaf");
        let t = String::from("aaa");
        assert_eq!(Solution::append_characters(s, t), 0);
    }

    #[test]
    fn test_all_characters_in_t_are_in_s_but_not_in_order() {
        let s = String::from("abacadaeaf");
        let t = String::from("fa");
        assert_eq!(Solution::append_characters(s, t), 1);
    }

    #[test]
    fn test_partial_match_at_beginning_of_s() {
        let s = String::from("abc");
        let t = String::from("abf");
        assert_eq!(Solution::append_characters(s, t), 1);
    }

    #[test]
    fn test_partial_match_at_end_of_s() {
        let s = String::from("abcdef");
        let t = String::from("defg");
        assert_eq!(Solution::append_characters(s, t), 1);
    }
}


pub struct Solution;

impl Solution {
    pub fn append_characters(s: String, t: String) -> i32 {
        let mut point1: usize = 0;
        let mut point2: usize = 0;

        while point1 < s.len() && point2 < t.len() {
            if &s[point1..point1 + 1] == &t[point2..point2 + 1] {
                point1 += 1;
                point2 += 1;
            } else {
                point1 += 1;
            }
        }

        (t.len() - point2) as i32
    }
}