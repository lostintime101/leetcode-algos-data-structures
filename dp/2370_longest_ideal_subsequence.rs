impl Solution {
    pub fn longest_ideal_string(s: String, k: i32) -> i32 {

        let mut alpha:[i32; 26] = [0; 26];

        for l in s.chars() {
            let curr = l as usize - 97;

            let low = usize::max(0, curr.checked_sub(k as usize).unwrap_or(0));
            let high = usize::min(25, curr + k as usize);

            let slice = &mut alpha[low..=high];
            if let Some(max_value) = slice.iter().max() {
                *alpha.get_mut(curr).unwrap() = *max_value + 1;
            }

        }

        if let Some(ans) = alpha.iter().max() {
            *ans
        } else {
            0
        }

    }
}