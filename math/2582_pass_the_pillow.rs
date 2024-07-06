impl Solution {
    pub fn pass_the_pillow(n: i32, time: i32) -> i32 {

        let place = time % (n-1);
        let rounds = time / (n-1);

        if (rounds % 2) != 0 {
            return n - place;
        } else {
            return 1 + place;
        }

    }
}