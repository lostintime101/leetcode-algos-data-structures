impl Solution {
    pub fn is_n_straight_hand(mut hand: Vec<i32>, group_size: i32) -> bool {

        let mut counts = hand.clone();
        counts.sort();

        // println!("{:?}", counts);

        for (start) in 0..counts.len() {

            let v = counts[start];
            if v == -1 {
                continue;
            }

            let mut end = start+1;
            let mut count = 1;
            let mut curr_v = v+1;

            while count < group_size && end < hand.len() {

                if counts[end] == curr_v {
                    curr_v += 1;
                    count += 1;
                    counts[end] = -1;
                }

                end += 1;
            }

            if count != group_size {
                return false;
            }

        }

        true

    }
}