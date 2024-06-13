impl Solution {
    pub fn min_moves_to_seat(mut seats: Vec<i32>, mut students: Vec<i32>) -> i32 {

        seats.sort();
        students.sort();

        let mut ans:i32 = 0;
        for i in 0.. seats.len() {
            ans += i32::abs(seats[i] - students[i]);
        }

        ans

    }
}