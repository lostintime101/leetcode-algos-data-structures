impl Solution {
    pub fn min_falling_path_sum(mut matrix: Vec<Vec<i32>>) -> i32 {

        let ROWS = matrix.len();
        let COLS = matrix[0].len();

        for row in 1..ROWS {
            for col in 0..COLS {

                let mut left = i32::MAX;
                let mut right = i32::MAX;
                let mut center = matrix[row-1][col];

                if col != 0 {
                    left = matrix[row-1][col-1];
                }
                if col != COLS-1 {
                    right = matrix[row-1][col+1];
                }

                matrix[row][col] += [left, right, center].iter().cloned().min().unwrap();
            }
        }

        matrix[ROWS - 1].iter().cloned().min().unwrap()

    }
}