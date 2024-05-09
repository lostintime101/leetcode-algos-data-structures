impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {

        happiness.sort_unstable();
        happiness.reverse();

        let hap2 = &mut happiness[0..k as usize];

        for (i,v) in hap2.iter_mut().enumerate() {

            if let Some(value) = v.checked_sub(i as i32) {
                if value < 0 {
                    *v = 0;
                }
                else {
                    *v = value;
                }
            } else {
                *v = 0;
            }

        }


        hap2.iter().map(|&a| a as i64).sum()
    }
}